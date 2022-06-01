import "./App.css";
import MUIDataTable from "mui-datatables";
import Grid from "@mui/material/Grid";
import submissions from "./data/submissions.json";
import { FaPython } from "react-icons/fa";
import { FaJava } from "react-icons/fa";
import { SiMicrosoftsqlserver } from "react-icons/si";
import { SiMysql } from "react-icons/si";
import Link from "@mui/material/Link";

const URL = "https://leetcode.com/problems/";

const options = {
  filter: true,
  filterType: "multiselect",
  responsive: "standard",
  fixedHeader: true,
  fixedSelectColumn: true,
  tableBodyHeight: "500px",
  selectableRows: false,
};

const columns = [
  {
    name: "timestamp",
    options: {
      filter: false,
    },
  },
  {
    name: "title",
    options: {
      filter: false,
      customBodyRender: (value) => (
        <Link
          href={URL + value.toLowerCase().split(" ").join("-")}
          underline="none"
        >
          {value}
        </Link>
      ),
    },
  },
  {
    name: "status",
    options: {
      filter: true,
    },
  },
  {
    name: "lang",
    options: {
      filter: true,
      customBodyRender: (value) => {
        if (value === "python3") {
          return <FaPython size={25} />;
        } else if (value === "java") {
          return <FaJava size={25} />;
        } else if (value === "mysql") {
          return <SiMysql size={25} />;
        } else if (value === "mssql") {
          return <SiMicrosoftsqlserver size={25} />;
        }
      },
    },
  },
  {
    name: "runtime",
    options: {
      filter: false,
    },
  },
  {
    name: "memory",
    options: {
      filter: false,
    },
  },
];

function App() {
  return (
    <div className="App">
      <Grid container spacing={4}>
        <Grid item xs={14}>
          <MUIDataTable
            title="LeetCode"
            data={submissions}
            columns={columns}
            options={options}
          />
        </Grid>
      </Grid>
    </div>
  );
}

export default App;
