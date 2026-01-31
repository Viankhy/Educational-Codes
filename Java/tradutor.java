import java.util.Arrays;

import javax.swing.JOptionPane;

public class tradutor {
    public static void main(String[] arg) {
        // Banco de dados
        String[] portugues = {"cachorro", "gato", "casa", "carro", "comida", "água"};
        String[] espanhol = {"perro", "gato", "casa", "coche", "comida", "agua"};
        String[] english = {"dog", "cat", "house", "car", "food", "water"};
        // Fim do banco de dados

        // // // // //

        // Inicio do Loop com uma trava criada
        int trava = 0;
        while (trava < 1) {
            int escolha = Integer.parseInt(JOptionPane.showInputDialog("Escolha uma das opções disponíveis: \n1. Tradutor \n2. Verificar palavras disponíveis \n3. Encerrar o programa"));

            // Tradutores
            if (escolha == 1) {
                String palavra = JOptionPane.showInputDialog(null, "Informa a palavra para traduzir:").toLowerCase(); // Recebe a palavra
                boolean disponivel = Arrays.asList(portugues).contains(palavra); // Checa se a palavra está disponível
                
                // Caso a palavra estiver disponível
                if (disponivel == true) {
                    // Recebe a lingua que deve ser usada
                    int lingua = Integer.parseInt(JOptionPane.showInputDialog("Para qual lingua você gostaria de traduzir?\n1. Espanhol\n2. Inglês"));

                    switch (lingua) {
                        // Espanhol
                        case 1:
                            // Loop para checar se a palavra inserida está disponível
                            for (int i = 0; i < portugues.length; i++) {
                                if(palavra.matches(portugues[i])){
                                    palavra = espanhol[i]; // Troca a palavra pela tradução
                                    JOptionPane.showMessageDialog(null, "Palavra em espanhol: " + palavra); // Exibe a tradução
                                }
                            }
                            break;
                    
                        // Inglês
                        case 2:
                            // Loop para checar se a palavra inserida está disponível
                            for (int i = 0; i < portugues.length; i++) {
                                if(palavra.matches(portugues[i])){
                                    palavra = english[i]; // Troca a palavra pela tradução
                                    JOptionPane.showMessageDialog(null, "Palavra em inglês: " + palavra); // Exibe a tradução
                                }
                            }
                            break;

                        default:
                            break;
                    }
                }
                
                // Caso a palavra não estiver disponível
                else {
                    JOptionPane.showMessageDialog(null, "A palavra " + palavra + " não está disponível para tradução!");
                }
            }

            // Dicionário
            else if (escolha == 2) {
                JOptionPane.showMessageDialog(null, "Palavras disponíveis para tradução:\n" + Arrays.toString(portugues));
            }

            // Encerra o programa
            else if (escolha == 3) {
                JOptionPane.showMessageDialog(null, "Encerrando...");
                trava++;
            }

        }
    }
}