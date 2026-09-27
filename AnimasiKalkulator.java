import javafx.animation.FadeTransition;
import javafx.animation.TranslateTransition;
import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.layout.StackPane;
import javafx.stage.Stage;
import javafx.util.Duration;

public class AnimasiKalkulator extends Application {

    @Override
    public void start(Stage primaryStage) {
        // 1. Membuat komponen GUI (misal tombol angka di kalkulator)
        Button btnAngka = new Button("7");
        btnAngka.setStyle("-fx-font-size: 24px; -fx-padding: 20px;");

        // 2. Membuat Animasi Geser (Translate Transition)
        // Menampilkan efek tombol muncul dari bawah ke atas
        TranslateTransition geser = new TranslateTransition(Duration.millis(800), btnAngka);
        geser.setFromY(100); // Mulai dari koordinat Y = 100
        geser.setToY(0);     // Berakhir di posisi asli (0)

        // 3. Membuat Animasi Transparan ke Muncul (Fade Transition)
        FadeTransition muncul Perlahan = new FadeTransition(Duration.millis(800), btnAngka);
        munculPerlahan.setFromValue(0.0); // Awalnya tidak terlihat (transparan)
        munculPerlahan.setToValue(1.0);   // Menjadi terlihat sepenuhnya

        // 4. Menjalankan animasi secara bersamaan
        geser.play();
        munculPerlahan.play();

        // Menyusun Layout
        StackPane root = new StackPane();
        root.getChildren().add(btnAngka);
        Scene scene = new Scene(root, 300, 250);

        primaryStage.setTitle("Animasi JavaFX");
        primaryStage.setScene(scene);
        primaryStage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}
