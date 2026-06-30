# Tool-Call Evidence Ledger for CPU Agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `tool-call-evidence-ledger-for-cpu-agents-8bc3def4dc2f`
Run ID: `tool-call-evidence-ledger-for-cpu-agents-8bc3def4dc2f-20260608T153415183220+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/5bdd7ad33d59

## What looked useful

The prototype ledger detected all four tested tamper modes. At 20,000 events over three repeats, mean ledger write throughput was 2,040 events/s versus 2,999 events/s for plain JSONL, mean ledger verification throughput was 11,183 events/s versus 62,070 events/s, and storage expansion was 1.37x.

## Boundaries and scale limits

No real agent framework traces, no concurrent writers, no crash-recovery validation, no distributed anchoring, no log rotation, and no adversarial pre-anchor attacker model were tested. Results are synthetic and local to this CPU worker.

## Claim scope

Synthetic single-process CPU-agent tool-call traces up to 20,000 events show that a canonical JSON SHA-256 hash-chain ledger with separate evidence digests detects payload mutation, entry deletion, entry reorder, and evidence blob mutation while retaining usable CPU throughput.

## Why it stopped

No-paper closure: the result is a useful synthetic systems signal, but it is not a direct real-agent or robustness validation.

## Recommended next action

Run a bounded deepen follow-up on real CPU-agent tool-call traces with concurrent append and crash-recovery checks before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Trace and Crash-Recovery Validation for CPU Agent Evidence Ledgers
- Success threshold: Ledger detects all injected tamper and crash-corruption cases, sustains at least 1,000 writes/s on the CPU worker, keeps storage expansion below 2x, and produces verifier diagnostics that localize the first corrupted event.
- Stop condition: Stop if real-trace write throughput falls below 500 events/s, storage expansion exceeds 3x, or any payload mutation, deletion, reorder, missing evidence blob, or partial-write corruption is not detected.

## Evidence references

- Artifact root: `<local-path>/projects/tool-call-evidence-ledger-for-cpu-agents-8bc3def4dc2f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
