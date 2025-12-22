import java.util.ArrayList;
import javax.swing.JOptionPane;

/**
 * cadastra números inseridos pelo usuário
 * e verifica qual é o maior número.
 */

public class listaNumerica {
    public static void main(String[] arg) {
        ArrayList<Integer> numeros = new ArrayList<Integer>();

        int trava = 0; // Trava da estrutura de repetição
        int indicador = 1; // Indicador, pra melhorar o visual

        // Estrutura de repetição
        while (trava < 1) {
            try {
                // Entrada de número do usuário
                int numero = Integer.parseInt(JOptionPane.showInputDialog("Informe o " + indicador + "º número\n\"0\" para encerrar o programa."));

                // Verifica se a entrada foi 0
                if (numero == 0) {
                    trava++; // Aumenta o valor da trava, assim encerrando o código
                }
                // Verifica se o número é negativo
                else if (numero < 0) {
                    JOptionPane.showMessageDialog(null, "Número POSITIVO!");
                }

                // Verifica se o número é válido
                else {
                    numeros.add(numero); // Adiciona o número no Array
                    indicador++; // Aumenta o indicador. (Visual)
                }
            } catch (NumberFormatException error) { // Caixa que identifica uma entrada que não seja um número
                JOptionPane.showMessageDialog(null, "Por favor, informe um número inteiro positivo!");
            }
        }

        // Calcula e modifica a variável para exibir o maior número
        int maiorNumero = numeros.get(0); // Variável que pega o primeiro indíce do array
        for (int i = 0; i < numeros.size(); i++) { // Estrutura de repetição que roda de acordo o tamanho do array
            if (numeros.get(i) > maiorNumero) { // Verifica a posição do indice é maior que o primeiro indice
                maiorNumero = numeros.get(i); // Modifica a variável maiorNumero para se tornar o maior do Array
            }
        }

        JOptionPane.showMessageDialog(null, "O maior número foi: " + maiorNumero); // Exibe o maior número
        System.out.println(numeros); // Debug pra saber todos os números registrados
        // Por algum motivo os números maiores são expurgados da lista após serem verificados
        System.exit(0); // Encerra o código.
    }
}