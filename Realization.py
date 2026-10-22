interface Payment {
    void pay(double amount);
}

class CashPayment implements Payment {
    @Override
    public void pay(double amount) {
        System.out.println("Paid ₱" + amount + " in cash.");
    }
}

public class Main {
    public static void main(String[] args) {
        Payment payment = new CashPayment();
        payment.pay(500.00);
    }
}