# Local N-gram Speculative Draft with Accept/Reject Ledger

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `local-n-gram-speculative-draft-with-accept-reject-ledger-822a8eeac017`
Run ID: `local-n-gram-speculative-draft-with-accept-reject-ledger-822a8eeac017-20260607T120405258423+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/e3d2b7fb95a6

## What looked useful

Ledger suppressed one stale prefix-token pair in recoverable_shift and improved tokens per target call from 4.0 to 8.9995, but on mixed_bursty it reduced tokens per target call by 0.4648 on average despite reducing rejections, indicating over-pruning.

## Boundaries and scale limits

No neural LM, tokenizer, KV-cache, batching, GPU kernel, serving latency, or real-corpus quality effects were measured. Runs used 10000 synthetic oracle verification steps across three seeds for each case.

## Claim scope

Synthetic n-gram-oracle evidence shows a persistent accept/reject ledger can improve local speculative drafting when a repeated prefix has a stale majority continuation but a correct minority continuation is present in the local table; the same simple policy can reduce accepted tokens per target call on stochastic bursty text.

## Why it stopped

Synthetic proxy evidence is mixed: the mechanism works in a recoverable repeated-prefix shift but the naive persistent rejection ledger regresses the primary throughput proxy on stochastic bursty text.

## Recommended next action

Stop this run as no-paper useful signal; next test should implement an adaptive/decayed ledger and require non-negative tokens-per-target-call delta on stochastic controls before neural-serving integration.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Adaptive rejection ledger for local n-gram speculative drafting
- Success threshold: Recoverable_shift tokens-per-target-call delta remains at least +4.0 while mixed_bursty tokens-per-target-call delta is >= 0.0 across seeds, with no output mismatch in a small neural-LM harness.
- Stop condition: Stop if adaptive policies still produce negative tokens-per-target-call deltas on mixed_bursty or require ledger growth that scales linearly with generated tokens without bounded pruning.

## Evidence references

- Artifact root: `<local-path>/projects/local-n-gram-speculative-draft-with-accept-reject-ledger-822a8eeac017`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
