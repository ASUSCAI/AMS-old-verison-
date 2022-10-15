import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public class App {
    public static void main(String[] args) {
        Connection connection = null;
        try {
            // create a database connection
            connection = DriverManager.getConnection("jdbc:sqlite:sample.db");
            Statement statement = connection.createStatement();
            statement.setQueryTimeout(30); // set timeout to 30 sec.

            statement.executeUpdate("DROP TABLE IF EXISTS Students");
            statement.executeUpdate("CREATE TABLE Students (id INTEGER, name TEXT)");
            statement.executeUpdate("INSERT INTO Students VALUES(1, 'John Doe')");
            statement.executeUpdate("INSERT INTO Students VALUES(2, 'Bob Good')");
            ResultSet rs = statement.executeQuery("SELECT * FROM Students");
            while (rs.next()) {
                // read the result set
                System.out.println("name: " + rs.getString("name"));
                System.out.println("id: " + rs.getInt("id"));
            }
        } catch (SQLException e) {
            // if the error message is "out of memory",
            // it probably means no database file is found
            System.err.println(e.getMessage());
        } finally {
            try {
                if (connection != null)
                    connection.close();
            } catch (SQLException e) {
                // connection close failed.
                System.err.println(e.getMessage());
            }
        }
    }
}