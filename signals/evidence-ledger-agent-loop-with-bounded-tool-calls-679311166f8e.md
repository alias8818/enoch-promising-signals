# Evidence-Ledger Agent Loop with Bounded Tool Calls

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `evidence-ledger-agent-loop-with-bounded-tool-calls-679311166f8e`
Run ID: `evidence-ledger-agent-loop-with-bounded-tool-calls-679311166f8e-20260527T162927162298+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/4449d4107a57

## What looked useful

Across 20 grid cells and 100,000 synthetic tasks, the evidence ledger beat transcript search in 16/20 cells with +6.248 percentage-point mean accuracy and beat the stronger low-confidence heuristic in 12/20 cells with +1.018 percentage-point mean accuracy. It eliminated duplicate calls, but lost at high budget/low noise because early stopping left useful extra calls unused.

## Boundaries and scale limits

The evidence is synthetic and policy-coded. It does not test real LLM planning, natural-language extraction, public QA benchmarks, real retrieval APIs, source correlation, latency, or stronger structured-state baselines. It is not publication-grade validation.

## Claim scope

In a deterministic synthetic QA benchmark with noisy search, targeted verification, and hard tool-call budgets of 4-8 calls, an explicit evidence-ledger policy reduced duplicate calls to zero and improved mean accuracy versus transcript search; it improved accuracy versus a low-confidence heuristic mainly under tighter or noisier budgets.

## Why it stopped

No-paper useful signal: the local synthetic experiment supports a bounded mechanism but is not direct real-agent evidence and shows mixed results against the stronger heuristic.

## Recommended next action

Run a bounded real-agent follow-up on a public tool-use or retrieval QA benchmark, preserving the same ledger-versus-baseline comparison and adding ablations for early stopping and duplicate-call avoidance.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-agent evidence-ledger loop on bounded retrieval QA
- Success threshold: Ledger policy improves accuracy by at least 3 percentage points over the strongest baseline at one tight budget without reducing supported-answer rate, and duplicate-call rate falls by at least 30%.
- Stop condition: Stop if the ledger fails to beat the strongest baseline on accuracy in two representative tight-budget settings or if reduced duplicate calls do not translate into correctness/support gains.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-agent-loop-with-bounded-tool-calls-679311166f8e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
