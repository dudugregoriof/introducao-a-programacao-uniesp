import java.util.Scanner;

public class atividadeAula2 {
    public static void main(String[] args) {
        Scanner ler = new Scanner(System.in);

        System.out.println("Digite seu nome: ");
        String nome = ler.next();

        System.out.println("Digite seu endereço: ");
        String endereco = ler.next();

        System.out.println("O que você está cursando? ");
        String curso = ler.next();

        System.out.println("Digite sua idade: ");
        int idade = ler.nextInt();

        boolean isRegularizado  = true;
        if(isRegularizado && idade  >= 18) {
            System.out.println("Cadastro realizado com sucesso!");
        } else {
            System.out.println("Por favor, se dirigir a secretaria e preencher declaração com a assinatura do responsável.");
        }

    }
}
