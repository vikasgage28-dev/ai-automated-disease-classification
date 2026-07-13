import { useState } from 'react';
import Header from './components/Header';
import SymptomInput from './components/SymptomInput';
import ResultCard from './components/ResultCard';
import { classifySymptoms } from './services/api';
import type { DiseaseResult } from './services/api';

function App() {
  const [symptoms, setSymptoms] = useState('');
  const [results, setResults] = useState<DiseaseResult[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleSubmit = async (text: string) => {
    setLoading(true);
    setError('');
    setResults([]);
    try {
      const data = await classifySymptoms(text);
      const topScore = data.results[0]?.confidence ?? 0;
      if (topScore < 0.1) {
        setError('No meaningful symptoms detected. Please describe your symptoms in plain English — e.g. "I have fever and headache".');
      } else {
        setResults(data.results);
      }
    } catch {
      setError('Could not connect to the AI backend. Make sure uvicorn is running.');
    } finally {
      setLoading(false);
    }
  };

  const handleReset = () => {
    setSymptoms('');
    setResults([]);
    setError('');
  };

  return (
    <div className="min-h-screen bg-slate-50">
      <Header />

      <main className="max-w-2xl mx-auto px-4 py-8 flex flex-col gap-5">
        <SymptomInput
          onSubmit={handleSubmit}
          onReset={handleReset}
          loading={loading}
          value={symptoms}
          onChange={setSymptoms}
        />

        {error && (
          <div className="bg-red-50 border border-red-200 text-red-700 rounded-xl px-5 py-4 text-sm">
            ⚠️ {error}
          </div>
        )}

        {results.length > 0 && (
          <div className="flex flex-col gap-3">
            <div className="flex items-center gap-2 px-1">
              <span className="text-lg">🩺</span>
              <h2 className="text-base font-bold text-gray-700 uppercase tracking-wide">
                Top Matching Conditions
              </h2>
            </div>
            {results.map((result, i) => (
              <ResultCard key={result.disease} result={result} rank={i} />
            ))}
            <div className="bg-yellow-50 border border-yellow-200 rounded-2xl px-5 py-3 mt-1">
              <p className="text-xs text-yellow-700 text-center font-medium">
                ⚠️ For informational purposes only. Always consult a qualified medical professional.
              </p>
            </div>
          </div>
        )}
      </main>
    </div>
  );
}

export default App;
