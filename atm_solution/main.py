from atm import ATM

atm1 = ATM("Bader",800)
atm1.withdraw(452)
atm1.display_withdrawals()

atm2 = ATM("Golf",975)
atm2.withdraw(642)
atm2.display_withdrawals()

atm2.withdraw(1000)
atm1.display_withdrawals()

