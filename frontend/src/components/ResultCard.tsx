import type { DiseaseResult } from '../services/api';

interface Props {
  result: DiseaseResult;
  rank: number;
}

const RANK_STYLES = [
  { medal: '🥇', bg: 'bg-amber-50', border: 'border-amber-200', badge: 'bg-amber-100 text-amber-700' },
  { medal: '🥈', bg: 'bg-slate-50', border: 'border-slate-200', badge: 'bg-slate-100 text-slate-600' },
  { medal: '🥉', bg: 'bg-orange-50', border: 'border-orange-200', badge: 'bg-orange-100 text-orange-700' },
];

function getBar(confidence: number) {
  if (confidence >= 0.5) return { color: 'bg-emerald-500', label: 'Strong match', text: 'text-emerald-600' };
  if (confidence >= 0.25) return { color: 'bg-amber-400', label: 'Moderate match', text: 'text-amber-600' };
  return { color: 'bg-rose-400', label: 'Weak match', text: 'text-rose-500' };
}

export default function ResultCard({ result, rank }: Props) {
  const pct = Math.round(result.confidence * 100);
  const style = RANK_STYLES[rank];
  const bar = getBar(result.confidence);

  return (
    <div className={`${style.bg} border ${style.border} rounded-2xl p-5 flex flex-col gap-3 shadow-sm`}>
      <div className="flex items-center justify-between">
        <div className="flex items-center gap-3">
          <span className="text-2xl">{style.medal}</span>
          <div>
            <p className="font-bold text-gray-800 text-base leading-tight">{result.disease}</p>
            <p className={`text-xs font-medium mt-0.5 ${bar.text}`}>{bar.label}</p>
          </div>
        </div>
        <span className={`text-2xl font-extrabold ${bar.text}`}>{pct}%</span>
      </div>

      <div className="w-full bg-white rounded-full h-2.5 shadow-inner">
        <div
          className={`${bar.color} h-2.5 rounded-full transition-all duration-700`}
          style={{ width: `${Math.max(pct, 2)}%` }}
        />
      </div>

      <p className="text-xs text-gray-400 text-right">
        Confidence score: {result.confidence.toFixed(4)}
      </p>
    </div>
  );
}
