export interface Doctor {
  id: number;
  name: string;
  specialty: string;
  image: string;
  description: string;
}

export interface Service {
  id: number;
  title: string;
  description: string;
  icon: string;
}

export interface Department {
  id: number;
  name: string;
  description: string;
  image: string;
}