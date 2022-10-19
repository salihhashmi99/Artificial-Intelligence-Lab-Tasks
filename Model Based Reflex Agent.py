class MailDelivery():
    def _init_(self, n):
        self.mails_limit = n
        print("Total emails that Rabot can deliver in one day are: ",n)

    def DoAction(self, todays_mails):
        if todays_mails > 0:
            print('There are', todays_mails, ' mails to be delivered')
            if todays_mails <= self.mails_limit:
                print('All emails will be delivered today')
            else:
                today_max = int(todays_mails - self.mails_limit)
                print('Only ', self.mails_limit, ' can be delivered today!')
                print('Remaining ', today_max, ' will be delivered Tomorrow')
        else:
            print('No emails will be delivered')

n=MailDelivery(60)
n.DoAction(23)
n.DoAction(75)


