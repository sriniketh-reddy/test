import streamlit as st
class Bank:
    def __init__(self):
        if "accBal" not in st.session_state:
            st.session_state.accBal = 10000

    def viewOptions(self):
        options = {
            "Deposit": self.deposit,
            "Withdraw": self.withdraw,
            "Balance Enquiry": self.balEnquiry,
            "Exit": self.exit_app
        }
        return options

    def validate(self, pin):
        if pin == 2909:
            return True
        else:
            return False

    def deposit(self, amount):
        if amount < 100:
            st.warning("Minimum deposit amount should be 100 Rs/-")
        elif amount % 100 != 0:
            st.warning("Depositing amount should be in multiples of 100 Rs/-")
        elif amount > 50000:
            st.warning("Maximum deposit amount is 50,000 Rs/-")
        else:
            st.session_state.accBal += amount
            st.success(f"{amount} Rs/- deposited successfully! Current Balance: {st.session_state.accBal} Rs/-")

    def withdraw(self, amount):
        if amount < 100:
            st.warning("Minimum withdrawal amount should be 100 Rs/-")
        elif amount % 100 != 0:
            st.warning("Withdrawal amount should be in multiples of 100 Rs/-")
        elif amount > 20000:
            st.warning("Maximum withdrawal transaction limit is 20,000 Rs/-")
        else:
            if st.session_state.accBal - amount < 500:
                st.warning(
                    f"Insufficient balance. Minimum balance of 500 Rs/- should be maintained. Current balance: {st.session_state.accBal} Rs/-")
            else:
                st.session_state.accBal -= amount
                st.success(f"{amount} Rs/- withdrawn successfully! Current Balance: {st.session_state.accBal} Rs/-")

    def balEnquiry(self):
        st.write(f"Your Account Balance is: {st.session_state.accBal} Rs/-")

    def exit_app(self):
        st.write("Thank you for using our service! Have a great day!")


st.title("Welcome to SBI Bank")

pin = st.text_input("Enter your PIN", type="password")

bank = Bank()

if pin:
    if bank.validate(int(pin)):
        st.success("PIN validated successfully!")

        option = st.selectbox("Select an option", options=["Deposit", "Withdraw", "Balance Enquiry", "Exit"])

        if option == "Deposit":
            amount = st.number_input("Enter amount to deposit", min_value=100)
            if st.button("Deposit"):
                bank.deposit(amount)

        elif option == "Withdraw":
            amount = st.number_input("Enter amount to withdraw", min_value=100)
            if st.button("Withdraw"):
                bank.withdraw(amount)

        elif option == "Balance Enquiry":
            if st.button("Check Balance"):
                bank.balEnquiry()

        elif option == "Exit":
            st.write("Thank you for using our service! Have a great day!")
            st.stop()

    else:
        st.error("Incorrect PIN! Please try again.")
