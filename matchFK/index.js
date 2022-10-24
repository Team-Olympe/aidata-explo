const mysql = require('mysql2/promise');

  // const getSample = (count, rows) => {
  //   let sample = new Set();
  //   let indexes = new Set();
  //   for (let i = 0; i < count; i++) {
  //     let randIndex
  //     do {
  //       randIndex = Math.floor(Math.random() * rows.length);
  //     } while (indexes.has(randIndex));

  //     indexes.add(randIndex);
  //     sample.add(rows[randIndex]);
  //   }
  //   return sample.values();
  // }


let CONFIG = {
  compare: {'Ventes': 'Code_Client', 'Client' : 'Code_Client'},
};
(async () => {
  const connection = await mysql.createConnection({ host: '127.0.0.1', port: "3307", user: 'myuser', password: "mypass", database: 'DATA' });


  const tables = Object.keys(CONFIG.compare);
  // const tables = (await connection.execute("SHOW TABLES"))[0].map(row => row.Tables_in_DATA);

  console.log('Fetching rows...');
  const rawData = (await Promise.all(tables.map(table  => connection.query(`SELECT * from ${table}`)))).map(result => result[0])

  const data = Object.fromEntries(tables.map((table, index) => [table, rawData[index]]));

  console.log('Extracting values...');
  const valueLeft = data[tables[0]].map(row => row[CONFIG.compare[tables[0]]]);
  const valueRight = data[tables[1]].map(row => row[CONFIG.compare[tables[1]]]);

  console.log('Comparing values...');
  const stats = valueLeft.reduce((acc, value) => {
    if(acc.cache.has(value) || valueRight.includes(value)) {
      acc.count += 1;
      acc.cache.add(value)
    }
    return acc;
  }, { count: 0, cache: new Set() });

  console.log(stats.count / valueLeft.length * 100);
})();
