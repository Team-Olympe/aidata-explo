import { Sequelize } from 'sequelize';

export const db = new Sequelize('explo-data_1', '288967', 'stur0MAU-heew7seeg', {
  host: 'mysql-explo-data.alwaysdata.net',
  dialect: 'mariadb',
  logging: false
});

export const queries = {
  sales: {
    byDay: db.query("SELECT DATE(Cle_Temps) as date, COUNT(*) as sales, SUM(Marge_Revient) as profit FROM `Ventes` GROUP BY date"),
    byMonth: db.query("SELECT DATE(Cle_Temps) as date, COUNT(*) as sales, SUM(Marge_Revient) as profit FROM `Ventes` GROUP BY YEAR(date), MONTH(date)"),
    byYear: db.query("SELECT DATE(Cle_Temps) as date, COUNT(*) as sales, SUM(Marge_Revient) as profit FROM `Ventes` GROUP BY YEAR(date)"),
  }
}

try {
  await db.authenticate();
  console.log('[DB] Connection has been established successfully.');
} catch (error) {
  console.error('[DB ]Unable to connect to the database:', error);
  process.exit(1);
}
