import timeseries from 'timeseries-analysis';
import { queries } from './lib/db.js';

(async () => {
  const [rawData] = await queries.sales.byMonth;

  console.log('-----------');
  const data = rawData.map(({ date, profit }) => ([new Date(date), parseFloat(profit)]));
  console.log("Data points", data.length)
  console.log(data);

  const timeserie = new timeseries.main(data);
  console.log("Average (mean):", timeserie.mean())
  console.log('-----------');

  var chart_url = timeserie.ma().chart();

  console.log(chart_url);
})();
