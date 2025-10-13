import javax.swing.JOptionPane;

public class areaRestrita {
    public static void main(String[] arg) {
        // Código da estrutura condicional. é mais simples que os ultimos dois.

        // Usuário do sistema
        String login = "root@voidlinux";
        String password = "void_linux";

        int trava = 3;

        do {
            String loginInt = JOptionPane.showInputDialog("Login:");
            String passwordInt = JOptionPane.showInputDialog("Senha:");

            if (loginInt.equalsIgnoreCase(login) && passwordInt.equals(password)) {
                JOptionPane.showMessageDialog(null, "Bem-vindo(a) ao sistema Void Linux!\nUsuário: " + login + "\nSenha: *****linux");
                trava -= 4;
            }

            else {
                JOptionPane.showMessageDialog(null, "Login e/ou Senha inválida!");
                trava--;
            }

        } while (trava > 0);

        if (trava <= -1) {
            JOptionPane.showMessageDialog(null, "Sistema liberado.");
        }

        else {
            JOptionPane.showMessageDialog(null, "Número de tentativas excedida!");
        }

    }
}
