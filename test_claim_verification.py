# Create the file and copy and paste this code for testing purposes
from knowledge_storm.storm_wiki.modules.claim_verification import verify_claim
from knowledge_storm.interface import Information

claim = "Quantum computers use qubits to represent data."

info_list = [
    Information(
        url="https://www.ibm.com/quantum-computing/",
        snippets=["Quantum computers leverage qubits, which can represent both 0 and 1 simultaneously."],
        title="Quantum Computing Overview",
        description="An overview of quantum computing principles and technologies."
    ),
    Information(
        url="https://quantamagazine.org",
        snippets=["Qubits are fundamentally different from classical bits."],
        title="Quantum Bits Explained",
        description="A primer on qubit-based systems."
    )
]

result = verify_claim(claim, {info.url: info.to_dict() for info in info_list})
print(f"Claim: {claim}")
print(f"Trust Score: {result['trust_score']}")
print(f"Justification: {result['reason']}")
