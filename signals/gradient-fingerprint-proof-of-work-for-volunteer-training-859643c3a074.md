# Gradient-Fingerprint Proof-of-Work for Volunteer Training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `gradient-fingerprint-proof-of-work-for-volunteer-training-859643c3a074`
Run ID: `gradient-fingerprint-proof-of-work-for-volunteer-training-859643c3a074-20260529T005321716802+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `83`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/bc97cb3bdc1b

## What looked useful

Exact replay matched fingerprint bits perfectly, unrelated controls were near chance, and a public linear forgery matched 64/256-bit targets exactly and 1024-bit targets at about 99.9% while running much faster than gradient computation. This supports fingerprints as audit diagnostics but undermines a standalone public fingerprint proof-of-work construction.

## Boundaries and scale limits

Tested only synthetic data, one tiny MLP, one local GPU worker, five random seeds, and a simplified public/leaked-challenge forgery. No multi-worker volunteer setting, real dataset, language model, formal cryptographic protocol, or long training run was tested.

## Claim scope

Toy PyTorch evidence on a 9,610-parameter synthetic classification model shows random-projection gradient fingerprints are exact-replay diagnostic features but are not sufficient standalone public proof-of-work for volunteer training.

## Why it stopped

Proxy/early falsification: the tested public or leaked fingerprint constraints are cheaply satisfiable without training-like work, so the standalone proof-of-work claim is unsupported without a stronger protocol.

## Recommended next action

Stop this public-fingerprint PoW line as no-paper evidence; only continue with a bounded commit-reveal protocol test that hides challenges and includes update-quality acceptance checks.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Commit-Reveal Gradient Fingerprint Audit Against Low-Work Provers
- Success threshold: At least 95% honest acceptance, at most 1% adversarial acceptance across replay/fabrication/surrogate controls, and verifier cost below 10% of prover training cost on the bounded task.
- Stop condition: Stop negative if verifier recomputation cost approaches full training replay or any low-work adversary exceeds 1% acceptance at an honest acceptance threshold of at least 95%.

## Evidence references

- Artifact root: `<local-path>/projects/gradient-fingerprint-proof-of-work-for-volunteer-training-859643c3a074`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
