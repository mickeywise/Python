from fpdf import FPDF


class Bill:
    """
    Objects that contains data about a bill. such as
    total amount and period of the bill.
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    Create a flatmate person who lives in the flat
    and pays a share of the bill
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, flatmate2):
        weight = self.days_in_house / (self.days_in_house + flatmate2.days_in_house)
        to_pay = bill.amount * weight
        return  to_pay

class PDFReport:
    """
    Creates a PDF file that contain data about the
    flatmates such as their names, their due amount
    and the period of the bill
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):

        flatmate1_pay = str(round(flatmate1.pays(bill, flatmate2), 2))
        flatmate2_pay = str(round(flatmate2.pays(bill, flatmate1), 2))


        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()
        #Add image
        pdf.image("images.png", w=30, h=30)

        #Insert title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=0, align="C", ln=1)
        
        #Insert Period label and value
        pdf.set_font(family="Times", size=14, style='B')
        pdf.cell(w=100, h=80, txt="Period:", border=0)
        pdf.cell(w=150, h=80, txt=bill.period, border=0, ln=1)

        # Insert name and due amount of the first flatmate
        pdf.set_font(family="Times", size=12)
        pdf.cell(w=100, h=20, txt=flatmate1.name, border=0)
        pdf.cell(w=150, h=20, txt=flatmate1_pay, border=0, ln=1)

        # Insert name and due amount of the first flatmate
        pdf.cell(w=100, h=20, txt=flatmate2.name, border=0)
        pdf.cell(w=150, h=20, txt=flatmate2_pay, border=0, ln=1)

        pdf.output(self.filename)



the_bill = Bill(amount = 120, period = "April 2021")
john  = Flatmate(name="John", days_in_house=20)
mary = Flatmate(name="Mary", days_in_house=25)

print("John pays: ",john.pays(bill=the_bill, flatmate2=mary))
print("Mary pays: ",mary.pays(bill=the_bill, flatmate2=john))

pdf_report = PDFReport(filename="Report1.pdf")
pdf_report.generate(flatmate1=john, flatmate2=mary, bill=the_bill)
