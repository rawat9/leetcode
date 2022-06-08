import "./App.css";
import MUIDataTable from "mui-datatables";
import Grid from "@mui/material/Grid";
import submissions from "./data/submissions.json";
import {
  SiMysql,
  SiMicrosoftsqlserver,
  SiJavascript,
  SiPython,
  SiJava,
  SiOracle,
  SiGo,
  SiLeetcode,
} from "react-icons/si";
import Link from "@mui/material/Link";
import CodeDialog from "./CodeDialog";
import SyntaxHighlighter from "react-syntax-highlighter";
import atomOneDark from "react-syntax-highlighter/dist/esm/styles/hljs/atom-one-dark";
import Container from "@mui/system/Container";

const URL = "https://leetcode.com/problems/";

const options = {
  filter: true,
  filterType: "dropdown",
  responsive: "stacked",
  tableBodyHeight: "580px",
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
          return <SiPython size={25} />;
        } else if (value === "java") {
          return <SiJava size={25} />;
        } else if (value === "javascript") {
          return <SiJavascript size={25} />;
        } else if (value === "golang") {
          return <SiGo size={25} />;
        } else if (value === "mysql") {
          return <SiMysql size={25} />;
        } else if (value === "oracle") {
          return <SiOracle size={25} />;
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
  {
    name: "code",
    options: {
      filter: false,
      customBodyRender: (value, tableMeta, update) => {
        let rowIndex = Number(tableMeta.rowIndex);
        return (
          <CodeDialog
            content={
              <SyntaxHighlighter
                language={
                  submissions[rowIndex].lang === "python3"
                    ? "python"
                    : submissions[rowIndex].lang
                }
                style={atomOneDark}
              >
                {value}
              </SyntaxHighlighter>
            }
          >
            ;
          </CodeDialog>
        );
      },
    },
  },
];

function App() {
  return (
    <div className="App">
      <Container maxWidth="xl">
        <Grid item xs={12}>
          <MUIDataTable
            title={<SiLeetcode size={20} />}
            data={submissions}
            columns={columns}
            options={options}
          />
        </Grid>
      </Container>
    </div>
  );
}

export default App;
