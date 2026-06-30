# Sybil-Resistant Bounded Work Tokens for Volunteer CPU Training

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `sybil-resistant-bounded-work-tokens-for-volunteer-cpu-training-75bc1c0658e5`
Run ID: `sybil-resistant-bounded-work-tokens-for-volunteer-cpu-training-75bc1c0658e5-20260630T052320968890+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/00147a51e60a

## What looked useful

At 200 Sybils and 20% real attacker compute, identity quotas accepted 65.99% attacker token share (3.30x amplification), while bounded work tokens accepted 20.11% (1.006x amplification) with 94.0% honest throughput. A 1% false-accept stress case reached 25.29% attacker share at 1000 Sybils.

## Boundaries and scale limits

No real CPU proof, volunteer network, adversarial client, or training loop was implemented. Results depend on simulator assumptions; a stress run with 1% false-accept validation and 1000 Sybils exceeded a 1.25x amplification threshold.

## Claim scope

Mechanism-level Monte Carlo simulation: bounded work tokens with per-unit CPU challenge verification kept accepted attacker influence near real CPU share under low false-accept validation, while identity quotas amplified Sybil influence.

## Why it stopped

Local simulation supports the mechanism but is proxy evidence only, not a full validation or publication-grade result.

## Recommended next action

Stop as no-paper useful signal; next bounded evidence should implement an actual CPU challenge verifier and integrate it with a small training-loop scheduler under adversarial replay/fabrication clients.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Implement CPU Challenge Work Tokens in a Toy Training Scheduler
- Success threshold: Attacker accepted influence <= 1.10x real measured CPU share, honest throughput >= 85%, replay acceptance = 0, fabricated-work false acceptance <= 0.1% over a bounded local run.
- Stop condition: Stop negative if attacker influence exceeds 1.25x real measured CPU share, honest throughput falls below 75%, or replay/fabrication acceptance cannot be bounded below 0.1% without centralized trust assumptions.

## Evidence references

- Artifact root: `<local-path>/projects/sybil-resistant-bounded-work-tokens-for-volunteer-cpu-training-75bc1c0658e5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
