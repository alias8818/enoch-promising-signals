# CPU-Bounded Self-Verification Loop with Evidence Ledger

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-bounded-self-verification-loop-with-evidence-ledger-92543c90b01c`
Run ID: `cpu-bounded-self-verification-loop-with-evidence-ledger-92543c90b01c-20260610T195229251415+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/bc2b9d07cee3

## What looked useful

Verification plus early stopping is useful when reliable cheap checks exist and high per-item accuracy is more important than lowest-cost throughput; it improved accuracy and reduced cost versus retry-majority but did not beat one-shot on correct answers per cost unit. The ledger design produced independently verifiable chained evidence for each decision.

## Boundaries and scale limits

Synthetic proxy only: no LLM, no natural-language ambiguity, no real token accounting, no adversarial verifier beyond a 5% false-pass sensitivity condition, and exact verifier access to task ground truth.

## Claim scope

On generated deterministic arithmetic/algebra tasks with a controlled noisy solver and exact verifier, a CPU-bounded self-verification loop with an append-only evidence ledger improved per-item accuracy over one-shot and retry-majority baselines while using substantially less cost than retry-majority.

## Why it stopped

Closed as a proxy useful-signal result, not a full validation: evidence supports the mechanism only under synthetic deterministic conditions with an exact verifier.

## Recommended next action

Run a bounded direct model experiment on held-out answer-checkable tasks with token/wall-clock accounting and measured verifier false-pass rates; do not write a paper from the synthetic proxy alone.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct Model Test of Ledgered CPU-Bounded Verification
- Success threshold: Ledgered verification improves accuracy by at least 3 percentage points over the strongest matched-budget baseline while keeping cost per correct answer within 1.5x and verifier false-pass rate below 2%.
- Stop condition: Stop if verifier false-pass exceeds 5%, if accuracy gain is below 1 percentage point on two independent seeds/splits, or if cost per correct answer exceeds 2x the strongest baseline.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-bounded-self-verification-loop-with-evidence-ledger-92543c90b01c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
