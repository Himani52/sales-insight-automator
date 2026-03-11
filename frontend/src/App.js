import React, { useState } from "react";

function App() {
  const [file, setFile] = useState(null);
  const [summary, setSummary] = useState("");

  const uploadFile = async () => {
    const formData = new FormData();
    formData.append("file", file);
    formData.append("email", "himani252006@gmail.com");

    const response = await fetch("https://sales-insight-automator-er7n.onrender.com/upload", {
      method: "POST",
      body: formData
    });

    const data = await response.json();
    setSummary(data.ai_summary);
  };

  return (
    <div style={{ padding: "40px" }}>
      <h1>Sales Insight Automator</h1>

      <input
        type="file"
        onChange={(e) => setFile(e.target.files[0])}
      />

      <br /><br />

      <button onClick={uploadFile}>
        Upload CSV
      </button>

      <h3>Analysis Result</h3>
      <pre>{summary}</pre>
    </div>
  );
}

export default App;