import streamlit as st
import os
import sys

class Bank:
    def __init__(self, amount):
        self.balance = amount
        self.transactions = 0

    def incrementTransactions(self):
        self.transactions += 1

    def isInDepositRange(self, amount):
        return 100 <= amount <= 50000

    def isInWithdrawRange(self, amount):
        return 100 <= amount <= 20000

    def isMultipleOf100(self, amount):
        return amount % 100 == 0
    @staticmethod
    def validatePin(pin):
        return pin == pin

    def deposit(self, amount):
        if not self.isInDepositRange(amount):
            st.error("Your Deposit Amount should be in range 100-50K")
            return False
        elif not self.isMultipleOf100(amount):
            st.error("Your Deposit Amount should be a Multiple of 100")
            return False
        self.balance += amount
        st.success(f"Deposited {amount} successfully!")
        return True
    def withdraw(self, amount):
        if not self.isInWithdrawRange(amount):
            st.error("Your Withdrawal Amount should be in range 100-20K")
            return False
        elif not self.isMultipleOf100(amount):
            st.error("Your Withdrawal Amount should be a Multiple of 100")
            return False
        elif (self.balance - amount) < 500:
            st.error("You need to maintain minimum balance of 500 Rs after withdrawal")
            self.showBalance()
            return False
        elif self.transactions > 2:
            st.error("Exceeded Daily Transaction Limit!")
            return False
        else:
            self.balance -= amount
            self.incrementTransactions()
            st.success(f"Withdrawn {amount} successfully!")
            return True

    def showBalance(self):
        st.write(f"Your Current Balance: {self.balance}")


st.title("CVR ATM System")
pin = st.text_input("Enter your PIN", type="password", max_chars=4, key="pin_input")

if "is_pin_verified" not in st.session_state:
    st.session_state.is_pin_verified = False

if st.button("Verify PIN") or st.session_state.is_pin_verified:
    st.session_state.is_pin_verified = True
    pin_int = int(pin)
    if not Bank.validatePin(pin_int):
        st.error("Invalid PIN! Please try again.")
    else:
        if "user" not in st.session_state:
            st.session_state.user=Bank(amount=5000)
        st.success("PIN verified successfully!")
        st.subheader("ATM Operations")

        option = st.selectbox("Choose an operation", options=["Deposit", "Withdraw", "Balance Enquiry", "Quit"])
        if option == "Deposit":
            amount = st.number_input("Enter amount to deposit", step=100)
            if st.button("Deposit"):
                st.session_state.user.deposit(amount)

        elif option == "Withdraw":
            amount = st.number_input("Enter amount to withdraw", step=100)
            if st.button("Withdraw"):
                st.session_state.user.withdraw(amount)

        elif option == "Balance Enquiry":
            st.session_state.user.showBalance()

        elif option == "Quit":
            st.write("Thank you for using the ATM system. Happy Banking!")
            st.session_state.is_pin_verified = False
            st.rerun()