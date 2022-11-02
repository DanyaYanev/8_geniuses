using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Calc
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            double a, b;
            a = Convert.ToDouble(textBox1.Text);
            b = Convert.ToDouble(textBox2.Text);
            if (comboBox1.Text == "+")
            {
                textBox3.Text = Convert.ToString(a + b);
            }

            if (comboBox1.Text == "-")
            {
                textBox3.Text = Convert.ToString(a - b);
            }

            if (comboBox1.Text == "*")
            {
                textBox3.Text = Convert.ToString(a * b);
            }

            if (comboBox1.Text == "/")
            {
                textBox3.Text = Convert.ToString(a / b);
            }


            //switch (comboBox1.Text)
            {
                //case "+":
                    //textBox3.Text = Convert.ToString(a + b);
                    //break;

                //case "-":
                    //textBox3.Text = Convert.ToString(a - b);
                    //break;

                //case "*":
                    //textBox3.Text = Convert.ToString(a * b);
                    //break;

                //case "/":
                    //if (b == 0)
                        //MessageBox.Show("На ноль делить нельзя");
                    //textBox3.Text = Convert.ToString(a / b);
                    //break;
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            this.Close();
        }
    }
}
