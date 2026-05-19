# Tool-use ledger cuts 1B agent hallucinations

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `tool-use-ledger-cuts-1b-agent-hallucinations-0bf8f8438dcf`
Run ID: `tool-use-ledger-cuts-1b-agent-hallucinations-0bf8f8438dcf-20260518T210023528588+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/3a12a50e16d3

## What looked useful

The useful mechanism is evidence isolation: clean transcripts and isolated ledgers both scored 0 unsupported slots, while a ledger placed next to contradictory mutable notes still produced 84.0% unsupported slots.

## Boundaries and scale limits

Synthetic deterministic support tasks only; one 1.5B instruction model; greedy decoding; no live tool calls, real agent traces, long-horizon memory, model sweep, or production-scale evaluation.

## Claim scope

In a 60-case synthetic final-answer benchmark with Qwen/Qwen2.5-1.5B-Instruct, presenting authoritative tool observations as an isolated append-only ledger reduced unsupported JSON answer slots from 51.3% under a conflicted mutable transcript to 0.0%.

## Why it stopped

No-paper closure: this is a synthetic medium signal that supports a mechanism but does not directly validate the broad deployed-agent hallucination claim.

## Recommended next action

Run a bounded deepen follow-up on real or semi-real multi-turn tool-use traces where the ledger is programmatically isolated/retrieved into the final-answer context and compared against a transcript baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Programmatic isolated ledger on real multi-turn tool-use traces
- Success threshold: Isolated ledger condition reduces unsupported claim rate by at least 30% relative to conflicted transcript baseline with non-overlapping or clearly separated bootstrap 95% confidence intervals, while ledger-plus-noisy-context does not match isolated-ledger performance.
- Stop condition: Stop if real/semi-real traces show less than 10% absolute unsupported-claim reduction, or if the benefit only appears on templated synthetic tasks and not on natural traces.

## Evidence references

- Artifact root: `<local-path>/projects/tool-use-ledger-cuts-1b-agent-hallucinations-0bf8f8438dcf`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
