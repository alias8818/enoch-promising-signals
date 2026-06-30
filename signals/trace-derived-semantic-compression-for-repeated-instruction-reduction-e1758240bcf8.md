# Trace-Derived Semantic Compression for Repeated Instruction Reduction

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `trace-derived-semantic-compression-for-repeated-instruction-reduction-e1758240bcf8`
Run ID: `trace-derived-semantic-compression-for-repeated-instruction-reduction-e1758240bcf8-20260628T153430796210+0000`

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

- Provider-backed Research Facility batch: z-ai/glm-5.2: enoch://research-facility/provider/z-ai/glm-5.2/9ea8f3f1be6b

## What looked useful

Exact trace-derived instruction factoring is a practical low-risk compression mechanism for repeated controller prompts. Lossy semantic compression is not supported by this probe because relaxed clustering added little savings while introducing content divergence.

## Boundaries and scale limits

Single project, local prompt/trace artifacts only; no live model compliance test, no multi-project corpus, no latency/cost benchmark, and the active JSONL trace grows during execution.

## Claim scope

On this Enoch worker's local prompt pair, deterministic exact repeated-block factoring of controller instructions saved 47.26% of analyzed block tokens under persistent-cache accounting; on the active trace snapshot it saved 30.43%. Near-duplicate semantic clustering did not add safe savings at high similarity thresholds.

## Why it stopped

No-paper useful signal: local token compression is supported, but semantic/behavioral preservation was only proxied and is insufficient for publication-grade claims.

## Recommended next action

Run a bounded behavioral follow-up that rewrites repeated exact instruction blocks as dictionary references and measures task success, instruction compliance, and token cost against uncompressed prompts.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Behavioral Validation of Exact Instruction Reference Compression
- Success threshold: Compressed-reference prompts reduce input tokens by at least 25% with no more than a 2 percentage point drop in task success or instruction-compliance checks versus full prompts.
- Stop condition: Stop if compressed-reference prompts cause more than a 2 percentage point compliance/task-success drop, or if exact repeats across the frozen corpus yield less than 15% token savings.

## Evidence references

- Artifact root: `<local-path>/projects/trace-derived-semantic-compression-for-repeated-instruction-reduction-e1758240bcf8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
