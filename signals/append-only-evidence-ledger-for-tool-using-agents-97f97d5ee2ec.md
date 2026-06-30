# Append-Only Evidence Ledger for Tool-Using Agents

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `append-only-evidence-ledger-for-tool-using-agents-97f97d5ee2ec`
Run ID: `append-only-evidence-ledger-for-tool-using-agents-97f97d5ee2ec-20260613T120011957586+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/8f60b319249d

## What looked useful

Append-only evidence ledgers need a trusted baseline, signed checkpoint, or external transparency anchor. Hash chaining alone is insufficient because fully rewritten and rehashed ledgers can pass local verification.

## Boundaries and scale limits

Synthetic local ledger only; no real tool-agent traces, signed checkpoints, remote transparency log, concurrent writers, adversarial natural-language evidence, or large benchmark corpus.

## Claim scope

Dependency-free verifier on a deterministic synthetic four-entry evidence ledger with eight tamper mutations and one valid append control; anchored append-only prefix verification caught all tested tamper cases, while unanchored hash-chain verification missed fully rehashed rewrites.

## Why it stopped

Closed as no-paper useful signal: this synthetic proxy supports the anchored verifier mechanism but is not direct/full validation on real agents.

## Recommended next action

Run a bounded follow-up on real tool-agent traces with signed checkpoints and manually labeled unsupported-claim/tamper cases.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Signed-checkpoint evidence ledger on real tool-agent traces
- Success threshold: Detect at least 95% of labeled tamper or unsupported-claim cases with no more than 5% false rejection of valid append-only traces on a corpus of at least 100 traces.
- Stop condition: Stop if signed anchoring still misses more than 10% of rewrite or unsupported-claim cases, or if false rejection of valid traces exceeds 10% after schema/debug fixes.

## Evidence references

- Artifact root: `<local-path>/projects/append-only-evidence-ledger-for-tool-using-agents-97f97d5ee2ec`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
