class Farmer:
    def __init__(self, name, location, crop_or_animal, symptoms, image_path):
        self.name = name
        self.location = location
        self.crop_or_animal = crop_or_animal
        self.symptoms = symptoms.lower()
        self.image_path = image_path

class DiagnosisResult:
    def __init__(self, disease, treatment, vet_alert):
        self.disease = disease
        self.treatment = treatment
        self.vet_alert = vet_alert

class AIDiagnosisEngine:
    def analyze(self, farmer):
        s = farmer.symptoms
        disease = "Unknown Condition"
        treatment = "Consult local agricultural/veterinary officer for analysis."
        vet_alert = True

        if "spots" in s:
            disease = "Leaf Spot Disease"
            treatment = "Use copper-based fungicides and remove infected leaves."
            vet_alert = False
        elif "yellow" in s or "yellowing" in s:
            disease = "Nutrient Deficiency"
            treatment = "Apply NPK fertilizer. Test soil nutrients."
            vet_alert = False
        elif "insects" in s or "worms" in s or "bugs" in s:
            disease = "Pest Infestation"
            treatment = "Use neem oil or approved pesticides."
            vet_alert = False
        elif "curl" in s or "curled" in s:
            disease = "Aphid Attack"
            treatment = "Spray neem oil or insecticidal soap."
            vet_alert = False
        elif "cough" in s:
            disease = "Bovine Respiratory Disease"
            treatment = "Isolate affected animal and administer antibiotics."
        elif "fur loss" in s or "hair loss" in s:
            disease = "Mange / Skin Infection"
            treatment = "Apply anti-parasitic treatment and disinfect area."
        elif "skin color" in s or "discolor" in s:
            disease = "Fungal Skin Infection"
            treatment = "Use antifungal spray/ointment."
        elif "eye discharge" in s or "pink eye" in s:
            disease = "Conjunctivitis (Pink Eye)"
            treatment = "Clean eyes and apply antibiotic eye drops."
        elif "limp" in s or "hoof" in s or "swelling" in s:
            disease = "Hoof Disease"
            treatment = "Clean and bandage affected hoof. Give anti-inflammatory meds."

        return DiagnosisResult(disease, treatment, vet_alert)

class VetAlertSystem:
    def send_alert(self, farmer, result):
        print("🚨 VETERINARY ALERT")
        print(f"Farmer: {farmer.name}, Location: {farmer.location}")
        print(f"⚠  Issue: {result.disease} - Vet has been notified.")

def start_analysis():
    farmer_names = [
        "Ramesh Goud", "Saroja Amma", "Bheem Rao", "Padma Nayak", "Mallesh Yadav",
        "Anitha Bai", "Komuraiah", "Kavitha Devi", "Narsimha Reddy", "Lalitha Bai"
    ]

    farmer_locations = [
        "Mamidipally, Ranga Reddy", "Narsampet, Warangal", "Kodangal, Vikarabad",
        "Marpally, Sangareddy", "Bhupalpally, Jayashankar", "Adilabad, Adilabad",
        "Mahadevpur, Karimnagar", "Aswaraopet, Kothagudem", "Dubbak, Siddipet", "Devarakonda, Nalgonda"
    ]

    farm_reports = [
        ("Leaf Spot Disease", "Crop", "spots on leaves"),
        ("Bovine Respiratory Disease", "Livestock", "cough and wheezing"),
        ("Nutrient Deficiency", "Crop", "yellowing leaves"),
        ("Mange / Skin Infection", "Livestock", "fur loss on back"),
        ("Unknown Condition", "Livestock", "slight restlessness"),
        ("Pest Infestation", "Crop", "insects and bugs on crops"),
        ("Fungal Skin Infection", "Livestock", "skin discoloration"),
        ("Conjunctivitis (Pink Eye)", "Livestock", "eye discharge"),
        ("Aphid Attack", "Crop", "leaves are curled"),
        ("Hoof Disease", "Livestock", "limp and swelling in leg"),
    ]

    engine = AIDiagnosisEngine()
    alert_system = VetAlertSystem()

    print("🌾 AI Disease Diagnosis Report 🌿\n")
    for idx, (_, type_, symptoms) in enumerate(farm_reports, 1):
        farmer = Farmer(
            name=farmer_names[idx - 1],
            location=farmer_locations[idx - 1],
            crop_or_animal=type_,
            symptoms=symptoms,
            image_path=f"image_{idx}.jpg"
        )

        result = engine.analyze(farmer)

        print(f"Farmer Name: {farmer.name}")
        print(f"Location: {farmer.location}")
        print(f"Is it Crop or Livestock?: {farmer.crop_or_animal}")
        print(f"Describe Symptoms: {farmer.symptoms}")
        print(f"📷 Image Path: {farmer.image_path}\n")
        print(f"🧪 Detected Disease: {result.disease}")
        print(f"💊 Suggested Treatment: {result.treatment}")
        if result.vet_alert:
            alert_system.send_alert(farmer, result)
        else:
            print("✅ No vet alert required.")
        print("✅ Report auto-submitted.\n" + "-" * 50 + "\n")

if __name__ == "__main__":
   start_analysis()

