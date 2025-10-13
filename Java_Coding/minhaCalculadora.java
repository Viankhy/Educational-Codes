import javax.swing.JOptionPane;

public class minhaCalculadora {
    public static void main(String[] arg) {
        // Início do código.
        int trava = 1;
        
        do {
            int escolha = Integer.parseInt(JOptionPane.showInputDialog(null, "Olá usuário! Qual tipo de calculo você gostaria de fazer?\n1. Soma\n2. Subtração\n3. Multiplicação\n4. Divisão\n5. Sair"));

            switch (escolha) {
                // Código da soma
                case 1:
                        float num1Sum = Float.parseFloat(JOptionPane.showInputDialog(null, "Insira o primeiro número:"));
                        float num2Sum = Float.parseFloat(JOptionPane.showInputDialog(null, "Insira o segundo número"));

                        float calculoSum = num1Sum + num2Sum;

                        JOptionPane.showMessageDialog(null, "O resultado da soma entre o número " + num1Sum + " e o número " + num2Sum + ", é de: " + calculoSum);
                    break;
            
                // Código da subtração
                case 2:
                        float num1Sub = Float.parseFloat(JOptionPane.showInputDialog(null, "Insira o primeiro número:"));
                        float num2Sub = Float.parseFloat(JOptionPane.showInputDialog(null, "Insira o segundo número"));

                        float calculoSub = num1Sub - num2Sub;

                        JOptionPane.showMessageDialog(null, "O resultado da soma entre o número " + num1Sub + " e o número " + num2Sub + ", é de: " + calculoSub);
                    break;
                
                // Código da multiplicação
                case 3:
                        float num1Mult = Float.parseFloat(JOptionPane.showInputDialog(null, "Insira o primeiro número:"));
                        float num2Mult = Float.parseFloat(JOptionPane.showInputDialog(null, "Insira o segundo número"));

                        float calculoMult = num1Mult * num2Mult;

                        JOptionPane.showMessageDialog(null, "O resultado da soma entre o número " + num1Mult + " e o número " + num2Mult + ", é de: " + calculoMult);
                    break;

                // Código da divisão
                case 4:
                        float num1Div = Float.parseFloat(JOptionPane.showInputDialog(null, "Insira o primeiro número:"));
                        float num2Div = Float.parseFloat(JOptionPane.showInputDialog(null, "Insira o segundo número"));

                        float calculoDiv = num1Div / num2Div;

                        JOptionPane.showMessageDialog(null, "O resultado da soma entre o número " + num1Div + " e o número " + num2Div + ", é de: " + calculoDiv);
                    break;
                    
                // Código para encerrar o programa
                case 5:
                        JOptionPane.showMessageDialog(null, "Encerrando o programa...");
                        trava--;
                    break;
                                        
                // Se a entrada for diferente de qualquer opção disponível
                default:
                        JOptionPane.showMessageDialog(null, "Por favor, entre com um valor válido!");
                    break;
            }

        } while (trava > 0);
    }
}