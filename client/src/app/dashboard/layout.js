import Navbar from "@/Components/Navbar";
import styles from "../../css/dashboard.module.scss";

export default function RootLayout({ children }) {
  return (
    <html lang="en">
        <body >
          <div className={styles.dashboard}>
            <div>
            <Navbar/>
            {children}
            </div>
          </div>
        </body>
    </html>
  );
}
