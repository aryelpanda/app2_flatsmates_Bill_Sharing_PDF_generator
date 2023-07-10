from fpdf import FPDF

my_pdf = FPDF(orientation='P', unit='pt', format='A4')  # defoult parameters
my_pdf.add_page()  # creates a page in the pdf

# add some text
my_pdf.set_font(family='Times', size=24, style='B')
my_pdf.cell(w=200, h=80, txt="Flatemates Bill", border=1, align='C', ln=1)
my_pdf.cell(w=80, h=40, txt="Period", border=1)
my_pdf.cell(w=150, h=40, txt="March 2023", border=1)
my_pdf.output("bill.pdf")
