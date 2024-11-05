import tkinter as tk
from tkinter import ttk
import numpy as np

class MortgageCalculatorGUI:
    def __init__(self, root):
        self.root = root
        
        # Add language selection
        self.texts = {
            'cn': {
                'title': "房贷对比计算器",
                'loan_params': "贷款参数",
                'principal': "贷款本金:",
                'plan_a': "方案A:",
                'plan_b': "方案B:",
                'term_months': "期限(月):",
                'annual_rate': "年利率(%):",
                'display_freq': "显示频率:",
                'monthly': "每月",
                'yearly': "每年",
                'calculate': "计算对比",
                'results': "计算结果",
                'invalid_input': "请输入有效的数值！\n",
                'month': "月",
                'year': "年",
                'interest_diff': "累计利息差额(方案B-方案A)：",
                'principal_diff': "累计本金差额(方案B-方案A)：",
                'plan_b_paid': "方案B已还本金：",
                'plan_a_paid': "方案A已还本金：",
                'total_diff': "累计还款差额(方案B-方案A)：",
            },
            'en': {
                'title': "Mortgage Comparison Calculator",
                'loan_params': "Loan Parameters",
                'principal': "Principal:",
                'plan_a': "Plan A:",
                'plan_b': "Plan B:",
                'term_months': "Term(months):",
                'annual_rate': "Annual Rate(%):",
                'display_freq': "Display Frequency:",
                'monthly': "Monthly",
                'yearly': "Yearly",
                'calculate': "Calculate",
                'results': "Results",
                'invalid_input': "Please enter valid numbers!\n",
                'month': "Month",
                'year': "Year",
                'interest_diff': "Cumulative Interest Difference(B-A)：",
                'principal_diff': "Cumulative Principal Difference(B-A)：",
                'plan_b_paid': "Plan B Principal Paid：",
                'plan_a_paid': "Plan A Principal Paid：",
                'total_diff': "Total Payment Difference(B-A)：",
            }
        }
        
        # Create main container frame
        self.main_frame = ttk.Frame(root)
        self.main_frame.grid(row=0, column=0, sticky="nsew")
        
        # Add language selector in a separate frame
        self.lang_frame = ttk.Frame(self.main_frame)
        self.lang_frame.grid(row=0, column=0, sticky="nw", padx=5, pady=5)
        
        self.current_lang = tk.StringVar(value='cn')
        ttk.Radiobutton(self.lang_frame, text="中文", variable=self.current_lang, 
                       value='cn', command=self.update_language).grid(row=0, column=0)
        ttk.Radiobutton(self.lang_frame, text="English", variable=self.current_lang, 
                       value='en', command=self.update_language).grid(row=0, column=1)

        # Create content frame to hold the rest of the UI
        self.content_frame = ttk.Frame(self.main_frame)
        self.content_frame.grid(row=1, column=0, sticky="nsew")

        self.setup_ui()

    def setup_ui(self):

        lang = self.current_lang.get()
        self.root.title(self.texts[lang]['title'])
        
        # Clear existing content frame widgets
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        
        # Create input frame
        input_frame = ttk.LabelFrame(self.content_frame, text=self.texts[lang]['loan_params'], padding="10")
        input_frame.grid(row=0, column=0, padx=10, pady=5, sticky="nsew")
        
        # Principal
        ttk.Label(input_frame, text=self.texts[lang]['principal']).grid(row=0, column=0, sticky="w")
        self.principal = ttk.Entry(input_frame)
        self.principal.insert(0, "512000")
        self.principal.grid(row=0, column=1, padx=5, pady=5)
        
        # Plan A parameters
        ttk.Label(input_frame, text=self.texts[lang]['plan_a']).grid(row=1, column=0, sticky="w")
        ttk.Label(input_frame, text=self.texts[lang]['term_months']).grid(row=2, column=0, sticky="w")
        self.short_term = ttk.Entry(input_frame)
        self.short_term.insert(0, "180")
        self.short_term.grid(row=2, column=1, padx=5, pady=5)
        
        ttk.Label(input_frame, text=self.texts[lang]['annual_rate']).grid(row=3, column=0, sticky="w")
        self.short_rate = ttk.Entry(input_frame)
        self.short_rate.insert(0, "5.875")
        self.short_rate.grid(row=3, column=1, padx=5, pady=5)
        
        # Plan B parameters
        ttk.Label(input_frame, text=self.texts[lang]['plan_b']).grid(row=4, column=0, sticky="w")
        ttk.Label(input_frame, text=self.texts[lang]['term_months']).grid(row=5, column=0, sticky="w")
        self.long_term = ttk.Entry(input_frame)
        self.long_term.insert(0, "360")
        self.long_term.grid(row=5, column=1, padx=5, pady=5)
        
        ttk.Label(input_frame, text=self.texts[lang]['annual_rate']).grid(row=6, column=0, sticky="w")
        self.long_rate = ttk.Entry(input_frame)
        self.long_rate.insert(0, "6.75")
        self.long_rate.grid(row=6, column=1, padx=5, pady=5)
        
        # Display frequency
        ttk.Label(input_frame, text=self.texts[lang]['display_freq']).grid(row=7, column=0, sticky="w")
        self.display_freq = ttk.Combobox(input_frame, 
                                       values=[self.texts[lang]['monthly'], 
                                              self.texts[lang]['yearly']])
        self.display_freq.set(self.texts[lang]['yearly'])
        self.display_freq.grid(row=7, column=1, padx=5, pady=5)
        
        # Calculate button
        calculate_btn = ttk.Button(input_frame, text=self.texts[lang]['calculate'], 
                                 command=self.calculate)
        calculate_btn.grid(row=8, column=0, columnspan=2, pady=10)
        
        # Results area
        result_frame = ttk.LabelFrame(self.root, text=self.texts[lang]['results'], 
                                    padding="10")
        result_frame.grid(row=0, column=1, rowspan=2, padx=10, pady=5, sticky="nsew")
        
        self.result_text = tk.Text(result_frame, width=50, height=18)
        self.result_text.grid(row=0, column=0)

        
        # Add scrollbar
        scrollbar = ttk.Scrollbar(result_frame, orient="vertical", 
                                command=self.result_text.yview)
        scrollbar.grid(row=0, column=1, sticky="ns")
        self.result_text.configure(yscrollcommand=scrollbar.set)

    def calculate_monthly_interest(self, principal, annual_rate, total_months, current_month):
        monthly_rate = annual_rate / 12
        numerator = np.power(1 + monthly_rate, total_months) - np.power(1 + monthly_rate, current_month - 1)
        denominator = np.power(1 + monthly_rate, total_months) - 1
        return principal * monthly_rate * numerator / denominator

    def calculate_monthly_principal(self, principal, annual_rate, total_months, current_month):
        monthly_rate = annual_rate / 12
        numerator = np.power(1 + monthly_rate, current_month - 1)
        denominator = np.power(1 + monthly_rate, total_months) - 1
        return principal * monthly_rate * numerator / denominator

    def update_language(self):
        """Update UI text when language changes"""
        # for widget in self.root.winfo_children():
        #     if widget.winfo_class() != 'Frame':  # Preserve language selector frame
        #         widget.destroy()
        self.setup_ui()

    def calculate(self):
        lang = self.current_lang.get()
        self.result_text.delete(1.0, tk.END)
        
        try:
            principal = float(self.principal.get())
            short_term_months = int(self.short_term.get())
            short_term_rate = float(self.short_rate.get()) / 100
            long_term_months = int(self.long_term.get())
            long_term_rate = float(self.long_rate.get()) / 100
        except ValueError:
            self.result_text.insert(tk.END, self.texts[lang]['invalid_input'])
            return

        differences = [0.] * 5

        for month in range(1, min(short_term_months, long_term_months) + 1):
            differences[0] -= (self.calculate_monthly_interest(principal, short_term_rate, short_term_months, month) - 
                             self.calculate_monthly_interest(principal, long_term_rate, long_term_months, month))
            
            differences[1] -= (self.calculate_monthly_principal(principal, short_term_rate, short_term_months, month) - 
                             self.calculate_monthly_principal(principal, long_term_rate, long_term_months, month))
            
            differences[2] += self.calculate_monthly_principal(principal, short_term_rate, short_term_months, month)
            differences[3] += self.calculate_monthly_principal(principal, long_term_rate, long_term_months, month)
            
            short_term_payment = (self.calculate_monthly_principal(principal, short_term_rate, short_term_months, month) + 
                                self.calculate_monthly_interest(principal, short_term_rate, short_term_months, month))
            long_term_payment = (self.calculate_monthly_principal(principal, long_term_rate, long_term_months, month) + 
                               self.calculate_monthly_interest(principal, long_term_rate, long_term_months, month))
            differences[4] += short_term_payment - long_term_payment

            should_display = False
            if self.display_freq.get() == self.texts[lang]['monthly']:
                should_display = True
            elif self.display_freq.get() == self.texts[lang]['yearly'] and month % 12 == 0:
                should_display = True

            if should_display:
                result = (f"{self.texts[lang]['month']} {month}({self.texts[lang]['year']} {month//12}):\n"
                         f"{self.texts[lang]['interest_diff']}{differences[0]:.2f}\n"
                         f"{self.texts[lang]['principal_diff']}{differences[1]:.2f}\n"
                         f"{self.texts[lang]['plan_b_paid']}{differences[3]:.2f}\n"
                         f"{self.texts[lang]['plan_a_paid']}{differences[2]:.2f}\n"
                         f"{self.texts[lang]['total_diff']}{-differences[4]:.2f}\n"
                         f"----------------------------------------\n")
                self.result_text.insert(tk.END, result)

if __name__ == "__main__":
    root = tk.Tk()
    app = MortgageCalculatorGUI(root)
    root.mainloop()