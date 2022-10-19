using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace game
{
    internal class Program
    {
        static void Main(string[] args)
        {                      
            int i = 3;
            int k = 0;
            int password, lvl;
            double hp, hp2, ap, ap2, percent, percent2, dmg, dmg2, endDamage, endDamage2;
            int real_password = 135;
            Random rand = new Random();
            do                              
            {
                Console.Write("Пароль: ");
                password = int.Parse(Console.ReadLine());
                if (real_password == password)
                {
                    Console.WriteLine("Вход выполнен");
                    break;
                }
                else
                {
                    i--;
                    Console.WriteLine($"Неверно, осталось попыткок: {i}");
                }
            }
            while (i != 0);
            if (i == 0)
                Environment.Exit(0);               
            Console.WriteLine("Выберите уровень 1, 2"); 
            Console.Write("Уровень: ");
            lvl = int.Parse(Console.ReadLine());     
            switch (lvl)
            {
                case 1:                              
                    Console.Write("HP гладиатора: ");
                    hp = double.Parse(Console.ReadLine());
                    if (hp > 100 || hp <= 0)           
                    {
                        Console.WriteLine("HP может быть только от 1 до 100");
                        Environment.Exit(0);                   
                    }
                    Console.Write("Броня гладиатора: ");
                    ap = double.Parse(Console.ReadLine());
                    if (ap > 100 || ap <= 0)             
                    {
                        Console.WriteLine("AP может быть только от 1 до 100");
                        Environment.Exit(0);                    
                    }
                    percent = ap / 4;                       
                    dmg = rand.Next(1, 100);
                    endDamage = dmg * (1 - percent / 100);
                    Console.WriteLine($"Урон по гладиатору: {Math.Round(endDamage, 0)}");
                    if (hp < endDamage)                 
                        Console.WriteLine("HP гладиатора: 0");
                    else
                        Console.WriteLine($"HP гладиатора: {Math.Round(hp - endDamage, 0)}"); 
                    break;
                case 2:                                             
                    hp = rand.Next(1, 100);
                    Console.WriteLine($"HP первого гладиатора: {hp}");     
                    hp2 = rand.Next(1, 100);
                    Console.WriteLine($"HP второго гладиатора: {hp2}");
                    ap = rand.Next(1, 100);
                    Console.WriteLine($"Броня первого гладиатора: {ap}");
                    ap2 = rand.Next(1, 100);
                    Console.WriteLine($"Броня второго гладиатора: {ap2}");
                    dmg = rand.Next(1, 100);
                    percent = ap / 4;                                   
                    endDamage = dmg * (1 - percent / 100);            
                    hp = hp - endDamage;
                    Console.WriteLine($"Урон по первому гладиатору: {Math.Round(endDamage, 0)}");        
                    dmg2 = rand.Next(1, 100);
                    percent2 = ap2 / 4;
                    endDamage2 = dmg2 * (1 - percent2 / 100);
                    hp2 = hp2 - endDamage2;
                    Console.WriteLine($"Урон по второму гладиатору: {Math.Round(endDamage2, 0)}");               
                    if (hp > 0 && hp2 > 0)
                    {
                        Console.WriteLine($"Оба гладиатора выжили, у первого гладиатора осталось {Math.Round(hp, 0)} HP, у второго гладиатора осталось {Math.Round(hp2, 0)} HP");
                        break;
                    }
                    if (hp > 0 && hp > hp2)
                        Console.WriteLine($"Победил первый гладиатор, у него осталось {Math.Round(hp, 0)} HP");
                    else if (hp2 > 0 && hp2 > hp)
                        Console.WriteLine($"Победил второй гладиатор, у него осталось {Math.Round(hp2, 0)} HP");
                    else
                        Console.WriteLine($"Оба гладиатора проиграли");
                    break;
            }
        }
    }
}