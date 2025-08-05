
# 🔐 ChaCha20-Hash - Lightweight Cryptographic Hash Function based on ChaCha20

**ChaCha20-Hash** is a novel cryptographic hash function inspired by the **ChaCha20 stream cipher**. This project explores how ChaCha20's internal permutation structure can be repurposed to create a secure, fast, and efficient hash function that meets modern cryptographic standards.

---

## 📌 Table of Contents

- [📌 Table of Contents](#-table-of-contents)
- [🎯 Project Objective](#-project-objective)
- [🧠 Background & Motivation](#-background--motivation)
- [🧱 Methodology](#-methodology)
- [⚙️ Tech Stack](#️-tech-stack)
- [🧪 Evaluation Criteria](#-evaluation-criteria)
- [📊 Benchmarking Plan](#-benchmarking-plan)
- [📎 References](#-references)

---

## 🎯 Project Objective

- Develop a cryptographic hash function using **ChaCha20's quarter-round transformations**.
- Ensure core security properties:
  - Pre-image resistance
  - Collision resistance
  - Strong avalanche effect
- Implement and test the algorithm against standard cryptographic benchmarks.
- Compare performance with industry-standard hash functions like **SHA-256**, **SHA-3**, and **BLAKE2**.

---

## 🧠 Background & Motivation

Modern cryptographic systems rely heavily on secure hash functions for integrity, authentication, and digital signatures.  
ChaCha20 is a fast, secure stream cipher well-regarded in real-world applications (e.g., TLS, WireGuard, SSH). While not designed for hashing, its internal mixing structure offers promising properties for transformation-based hash design.

**ChaCha20-Hash** is an experimental design aimed at reusing **ChaCha20's proven cryptographic core** to explore a novel approach to hashing.

---

## 🧱 Methodology

### 🔸 Design
- Use a **sponge-like or HAIFA-inspired construction** to process input blocks.
- Define input padding, state initialization, and output extraction.
- Use ChaCha20's core transformations (quarter-rounds, rotations) for state mixing.

### 🔸 Implementation
- Implemented in **Python** for prototyping; future optimization in **Rust** or **C**.
- Modular design:
  - Input pre-processing
  - ChaCha-based state transformation
  - Output extraction (e.g., 256-bit or 512-bit hash)

### 🔸 Testing
- Validate security properties:
  - Collision and pre-image resistance
  - Avalanche effect
- Perform randomness analysis using:
  - **NIST STS**
  - **Dieharder**
  - **ENT**

---

## ⚙️ Tech Stack

| Component          | Technology         |
|-------------------|--------------------|
| Language           | Python (prototype), Rust or C (optimized) |
| Crypto Library     | PyCryptodome / RustCrypto / Custom |
| Testing Tools      | NIST STS, Dieharder, ENT |
| Documentation      | Markdown, LaTeX (reporting) |
| Version Control    | Git + GitHub |

---

## 🧪 Evaluation Criteria

| Property            | Evaluation Method                      |
|---------------------|----------------------------------------|
| Collision Resistance | Attempted collision generation        |
| Pre-image Resistance | Reversibility testing                 |
| Avalanche Effect     | Bit-flip + Hamming distance analysis  |
| Output Uniformity    | Entropy and frequency tests           |
| Performance          | Throughput in MB/s                    |

---

## 📊 Benchmarking Plan

- Compare **ChaCha20-Hash** against:
  - SHA-256
  - SHA-3
  - BLAKE2b
- Metrics:
  - Speed (MB/s)
  - Hash uniformity
  - Output entropy
  - Memory usage

---

## 📎 References

- Bernstein, D. J. (2008). [ChaCha: A variant of Salsa20](https://cr.yp.to/chacha/chacha-20080128.pdf)
- RFC 8439 – ChaCha20 and Poly1305 for IETF protocols
- Biham, E., & Dunkelman, O. (2007). The HAIFA construction
- NIST SP 800-22 – Statistical Testing Suite (STS)
- [Keccak Team – Sponge construction](https://keccak.team/keccak.html)