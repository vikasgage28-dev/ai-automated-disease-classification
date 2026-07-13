export default function Header() {
  return (
    <header className="bg-slate-800 text-white shadow-md">
      <div className="max-w-4xl mx-auto px-6 py-7 text-center">
        <div className="flex items-center justify-center gap-3 mb-2">
          <span className="text-3xl">🧬</span>
          <h1 className="text-xl font-bold tracking-tight text-white whitespace-nowrap">
            Automated Disease Classification from Symptoms Text
          </h1>
        </div>
        <p className="text-slate-400 text-sm">
          Classify diseases based on patient symptom descriptions using Hugging Face NLP models
        </p>
        <div className="flex justify-center gap-3 mt-4">
          {['🤗 HuggingFace', '🔒 GDPR Safe', '⚡ Runs Locally'].map((badge) => (
            <span key={badge} className="bg-slate-700 text-slate-300 text-xs px-3 py-1 rounded-full font-medium">
              {badge}
            </span>
          ))}
        </div>
      </div>
    </header>
  );
}
