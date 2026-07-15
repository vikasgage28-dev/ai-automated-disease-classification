import { useState } from 'react';

interface Props {
  onSubmit: (symptoms: string) => void;
  onReset: () => void;
  loading: boolean;
  value: string;
  onChange: (value: string) => void;
}

const EXAMPLES = [
  { label: '🤒 Flu', text: 'fever, headache and body aches' },
  { label: '❤️ Heart', text: 'chest pain and shortness of breath' },
  { label: '🌿 Skin', text: 'skin rash and itching' },
  { label: '🟡 Liver', text: 'yellow eyes and dark urine' },
  { label: '💧 Diabetes', text: 'frequent urination and extreme thirst' },
];

export default function SymptomInput({ onSubmit, onReset, loading, value, onChange }: Props) {
  const [inputError, setInputError] = useState('');

  const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    if (!value.trim()) {
      setInputError('Please enter a text to classify.');
      return;
    }
    setInputError('');
    onSubmit(value.trim());
  };

  const handleReset = () => {
    setInputError('');
    onReset();
  };

  return (
    <div className="bg-white rounded-3xl shadow-lg p-8 border border-gray-100">
      <div className="mb-5">
        <h2 className="text-xl font-bold text-gray-800">Describe your symptoms</h2>
        <p className="text-gray-400 text-sm mt-1">
          Use plain English to describe what you are feeling
        </p>
      </div>

      <form onSubmit={handleSubmit} className="flex flex-col gap-3">
        <textarea
          id="symptoms"
          name="symptoms"
          rows={4}
          value={value}
          onChange={(e) => onChange(e.target.value)}
          placeholder="e.g. I have chest pain and difficulty breathing..."
          className="w-full border border-gray-200 rounded-2xl px-4 py-3 text-gray-700 text-sm resize-none focus:outline-none focus:ring-2 focus:ring-teal-400 bg-gray-50 placeholder-gray-300"
        />
        <button
          type="submit"
          disabled={loading}
          className="w-full bg-teal-600 hover:bg-teal-700 disabled:opacity-50 text-white font-semibold py-3.5 rounded-2xl transition-all shadow-sm hover:shadow-md text-sm"
        >
          {loading ? '⏳ Analysing...' : '🔍 Classify Symptoms'}
        </button>

        {inputError && (
          <p className="text-red-500 text-xs text-center -mt-1">{inputError}</p>
        )}

        <button
          type="button"
          onClick={handleReset}
          disabled={!value.trim()}
          className="w-full py-3.5 rounded-2xl border border-gray-300 text-gray-500 hover:border-red-300 hover:text-red-500 hover:bg-red-50 disabled:opacity-40 disabled:cursor-not-allowed transition-all text-sm font-semibold"
        >
          ✕ Reset
        </button>
      </form>

      <div className="mt-5">
        <p className="text-xs text-gray-400 mb-3 font-medium uppercase tracking-wide">Try an example</p>
        <div className="flex flex-wrap gap-2">
          {EXAMPLES.map((ex) => (
            <button
              key={ex.label}
              onClick={() => onChange(ex.text)}
              className="text-xs bg-teal-50 hover:bg-teal-100 text-teal-700 px-3 py-1.5 rounded-full border border-teal-100 transition-all font-medium"
            >
              {ex.label}
            </button>
          ))}
        </div>
      </div>
    </div>
  );
}
