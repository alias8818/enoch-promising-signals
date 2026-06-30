# N-gram speculative draft for CPU agent inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-speculative-draft-for-cpu-agent-inference-79097c081cd1`
Run ID: `n-gram-speculative-draft-for-cpu-agent-inference-79097c081cd1-20260608T210342314678+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/0ff866bd4fb9

## What looked useful

The mechanism depends on repeated local sequence structure. Shuffled controls collapsed to about 1.0x, while structured traces showed measurable implied call reduction, so future work should target agent/tool-call transcripts rather than broad natural text.

## Boundaries and scale limits

No live model serving was benchmarked; tokenization was regex-based rather than model-tokenizer based; corpora were small local proxies; draft lookup overhead, logits verification cost, KV-cache effects, sampling behavior, and output-quality equivalence were not directly measured.

## Claim scope

Trace-replay evidence shows online n-gram speculative drafting can reduce implied target verification calls on repeated structured agent-like text, with 1.61x on a local Codex JSONL proxy and 5.68x on a highly repetitive generated agent-template control, but only 1.03x on natural literary text.

## Why it stopped

Trace replay supports a narrow mechanism but is not direct serving evidence; this is a bounded proxy result, not full validation.

## Recommended next action

Stop this run as no-paper useful signal; next run should implement the n-gram drafter in a CPU decoding loop with the real tokenizer and require wall-clock tokens/sec improvement on held-out agent traces.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct CPU-serving benchmark for n-gram speculative drafting on agent traces
- Success threshold: At least 1.20x wall-clock tokens/sec improvement on two held-out structured agent-trace sets, with no output divergence under deterministic decoding and less than 10% overhead from draft lookup.
- Stop condition: Stop if live CPU serving speedup is below 1.10x on both held-out trace sets or if draft lookup overhead erases target-call savings.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-speculative-draft-for-cpu-agent-inference-79097c081cd1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
