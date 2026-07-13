import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000';

export interface DiseaseResult {
  disease: string;
  confidence: number;
}

export interface ClassificationResponse {
  results: DiseaseResult[];
}

export async function classifySymptoms(
  symptoms: string
): Promise<ClassificationResponse> {
  const response = await axios.post(`${API_URL}/classify`, { symptoms });
  return response.data;
}
