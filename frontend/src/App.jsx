import { useState } from "react";

function App() {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [result, setResult] = useState(null);

  const generateQuestion = async () => {
    const res = await fetch("http://127.0.0.1:8000/generate-question", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ 
        domain: "data structures",
        level: "beginner"}),
    });

    const data = await res.json();
    setQuestion(data.question);
    setResult(null);
  };

  const evaluateAnswer = async () => {
    const res = await fetch("http://127.0.0.1:8000/evaluate-answer", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        question: question,
        user_answer: answer,
      }),
    });

    const data = await res.json();
    setResult(data.feedback);
  };

  return (
    <div style={{ padding: "40px", fontFamily: "Arial" }}>
      <h1>Online Interview Assistant</h1>

      <button onClick={generateQuestion}>
        Generate Question
      </button>

      {question && (
        <div style={{ marginTop: "20px" }}>
          <h3>Question:</h3>
          <p>{question}</p>

          <textarea
            rows="4"
            cols="60"
            placeholder="Type your answer here..."
            value={answer}
            onChange={(e) => setAnswer(e.target.value)}
          />

          <br /><br />

          <button onClick={evaluateAnswer}>
            Submit Answer
          </button>
        </div>
      )}

      {result && (
        <div style={{ marginTop: "30px", background: "#f4f4f4", padding: "20px" }}>
          <h3>Evaluation</h3>
          <p><strong>Score:</strong> {result.score}/10</p>
          <p><strong>Strengths:</strong> {result.strengths}</p>
          <p><strong>Weaknesses:</strong> {result.weaknesses}</p>
          <p><strong>Ideal Answer:</strong> {result.ideal_answer}</p>
        </div>
      )}
    </div>
  );
}

export default App;
