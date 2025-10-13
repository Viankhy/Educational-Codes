import javax.swing.JOptionPane;

public class calculoMedia {
    public static void main(String[] arg) {
        // Estrutura de repitação com uma trava.
        // Se trava for maior que 0, continuiar a estrutura de repetição
        int trava = 1;

        do {
            String escolha = JOptionPane.showInputDialog(null, "Bem-vindo(a) ao medidor de média.\nPara continuar digite \"Entrar\".\nPara encerrar digite \"Sair\".");

            // Se o usuário digitar "entrar", o código abaixo é iniciado
            if (escolha.equalsIgnoreCase("Entrar")) {
                int travaWhile = 1;

                // Variaveis usadas pro calculo
                int alunos = 0;
                float notas = 0;

                while (travaWhile > 0) {
                    String notaIn = JOptionPane.showInputDialog(null, "Digite \"Sair\" para calcular o resultado.\nInforme a nota (Entre 0 a 10) do " + (alunos + 1) + "º Aluno:");
                    
                    // Checa se usuário escolheu sair
                    // Roda primeiro que o float pq se não ele tentar checar um String no Float
                    if (notaIn.equalsIgnoreCase("Sair")) {
                        JOptionPane.showMessageDialog(null, "Processando dados...");
                        float calculo = notas / alunos;
                        JOptionPane.showMessageDialog(null, "A média da turma é de: " + calculo);
                        break;
                    }

                    // Faz o calculo e modifica as variáveis
                    else if (Float.parseFloat(notaIn) >= 0 && Float.parseFloat(notaIn) <= 10) {
                        notas += Float.parseFloat(notaIn);
                        alunos++;
                        System.out.println(alunos + " " + notas + " " + notaIn);
                    }
                    
                    // Se o usuário colocar qualquer coisa fora das opção disnponível
                    else {
                        JOptionPane.showMessageDialog(null, "Insira uma nota válida!");
                    }
                }
            }

            // Encerramento do código
            // ele diminui a trava de 1 pra 0, destravando o código e permitindo ele ser encerrado
            else if (escolha.equalsIgnoreCase("Sair")) {
                JOptionPane.showMessageDialog(null, "Encerrando o programa...");
                trava--;
            }

            // Se tentar colocar algo não previsto
            else {
                JOptionPane.showMessageDialog(null, "Insira uma opção válida!");
            }

        } while (trava > 0);
    }
}
