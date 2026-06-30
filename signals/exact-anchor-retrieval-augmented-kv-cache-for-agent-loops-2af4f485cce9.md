# Exact-Anchor Retrieval-Augmented KV Cache for Agent Loops

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `exact-anchor-retrieval-augmented-kv-cache-for-agent-loops-2af4f485cce9`
Run ID: `exact-anchor-retrieval-augmented-kv-cache-for-agent-loops-2af4f485cce9-20260523T080004646884+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/11eaccdf4394

## What looked useful

Across 10 random decoder seeds, exact prefix reuse stayed within float tolerance (worst max absolute logit difference 5.96e-07), while shifted exact-anchor naive reuse produced large logit differences in every seed (minimum max difference 0.684, mean shifted mean difference 0.186) and changed top-1 next token in 4 of 10 seeds. A 40-turn synthetic trace showed safe prefix caching saved 22.8% of prefill tokens, while an unsafe all-anchor oracle would save 30.8%; the extra shifted-anchor savings are not valid under naive KV retrieval.

## Boundaries and scale limits

Randomly initialized small decoder, synthetic agent-loop token accounting, no real pretrained LLM serving trace, and no production throughput measurement. Timing was dominated by tiny-model framework overhead and should not be treated as a speed claim.

## Claim scope

In a small GPT-2-style causal decoder probe, exact KV reuse is logit-equivalent for true repeated prefixes, but naive retrieval and reuse of exact anchor KV blocks at shifted positions is not logit-equivalent. The useful scoped result is a correctness warning, not a serving-speed validation.

## Why it stopped

Proxy/direct small-run closure: direct small-model evidence falsifies naive shifted exact-anchor KV retrieval, while the only supported mechanism is ordinary prefix caching. This is not a full validation of all possible anchor-aware cache designs.

## Recommended next action

Stop this run as no-paper useful evidence; any next bounded test should implement a position/context-aware non-prefix anchor reuse mechanism and require exact-logit equivalence against a standard prefix-cache baseline before measuring speed.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Position-aware exact-anchor KV reuse equivalence test
- Success threshold: For non-prefix anchors, max absolute logit difference <= 1e-4 versus full prefill on at least 99% of placements, with a measured valid latency or prefill-token reduction beyond prefix caching.
- Stop condition: Stop if the position/context-aware variant cannot meet exact-logit tolerance on controlled prompts or if savings beyond prefix caching are below 5% on realistic agent-loop traces.

## Evidence references

- Artifact root: `<local-path>/projects/exact-anchor-retrieval-augmented-kv-cache-for-agent-loops-2af4f485cce9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
