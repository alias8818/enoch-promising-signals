# Layered agent memory: retrieval-only vs trace-derived semantic compression on repeated tasks

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `layered-agent-memory-retrieval-only-vs-trace-derived-semantic-compression-on-repeated-tasks-d68728863883`
Run ID: `layered-agent-memory-retrieval-only-vs-trace-derived-semantic-compression-on-repeated-tasks-d68728863883-20260628T194851920367+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/b7567edcb0a4

## What looked useful

Compression into signature-to-action rules reached 1.000 mean accuracy across 50 high-drift seeds versus 0.117 for prompt-only retrieval and 0.419 for retrieval with probe signatures, with 32.5x fewer stored tokens and about 84.9x fewer per-task context tokens than retrieval in the high-drift setting.

## Boundaries and scale limits

The benchmark is synthetic and CPU-only. Semantic signatures are provided by the simulator rather than extracted from real LLM/tool traces. Results do not validate production agent memory, embedding retrieval, hybrid memory, evolving task families, or long-horizon compression errors.

## Claim scope

In a deterministic synthetic repeated-task benchmark with 12 task families and simulator-provided trace signatures, trace-derived semantic compression selected correct repeated-task strategies more accurately than raw full-trace retrieval while using much less memory and context.

## Why it stopped

No-paper useful signal: the local proxy supports the mechanism, but the signature extractor is simulated, so this is not direct validation of real layered agent memory.

## Recommended next action

Run a bounded deepen follow-up on real agent traces with an actual semantic extractor and embedding retrieval baseline before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-trace semantic compression versus embedding retrieval for repeated agent tasks
- Success threshold: Compression accuracy within 5 percentage points of the best retrieval baseline or better, with at least 5x lower per-task context tokens and no more than 10% strategy errors attributable to incorrect compression.
- Stop condition: Stop if automatic compression causes more than 10% unrecoverable strategy errors or fails to reduce context tokens by 5x on the real-trace benchmark.

## Evidence references

- Artifact root: `<local-path>/projects/layered-agent-memory-retrieval-only-vs-trace-derived-semantic-compression-on-repeated-tasks-d687`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
