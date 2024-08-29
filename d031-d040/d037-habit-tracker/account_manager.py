from account import Account
import pandas

CONFIG_FILE = 'output/accounts.csv'


class AccountManager:
    def __init__(self):
        self.accounts: list[Account] = []
        self.load_data()

    def load_data(self) -> None:
        try:
            data = pandas.read_csv(CONFIG_FILE)

            for _, row in data.iterrows():
                self.accounts.append(
                    Account(row['NAME'], row['TOKEN']))
        except FileNotFoundError:
            # ignore
            pass

    def account_exists(self, username: str) -> bool:
        matching_accounts = [
            a
            for a in self.accounts
            if a.username == username]

        return len(matching_accounts) > 0

    def get_account(self, username: str) -> Account | None:
        for a in self.accounts:
            if a.username == username:
                return a

        return None

    def store_account(self, account):
        self.accounts.append(account)
        self.save_accounts()

    def save_accounts(self):
        df = pandas.DataFrame([a.as_dict() for a in self.accounts])
        df.to_csv(CONFIG_FILE, index=False)

    def remove_account(self, account):
        self.accounts.remove(account)
        self.save_accounts()
