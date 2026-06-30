# Suffix-tree speculative decoding vs exact no-speculation on local LLM

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-tree-speculative-decoding-vs-exact-no-speculation-on-local-llm-edc3e66591e5`
Run ID: `suffix-tree-speculative-decoding-vs-exact-no-speculation-on-local-llm-edc3e66591e5-20260621T204600379772+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/21ef13b04662

## What looked useful

History/suffix drafting can propose acceptable continuations and reduce target forward calls on repetitive contexts, but exactness is fragile in this local cached chunk-verification harness; a non-toy pretrained model diverged from exact no-spec greedy decoding on repeated code.

## Boundaries and scale limits

No 7B+ chat model, no production suffix-tree implementation, no sampling-distribution validation, and no native inference-engine KV-cache crop/replay implementation. The suffix index is an ngram-style token history lookup proxy for suffix-tree drafting.

## Claim scope

Bounded local greedy-decoding benchmark using a Python suffix/ngram history drafter around Hugging Face causal LMs. Tiny GPT-2 matched exact sequential greedy decoding and reduced target forwards, but distilgpt2 failed exact greedy equality on repeated-code prompts.

## Why it stopped

Proxy/local benchmark found forward-call reduction but failed exact greedy equality on distilgpt2 repeated-code prompts, so this is an early falsification of the exact suffix-tree speculative decoding claim rather than a full validation.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should implement the drafter in a native inference stack with verified KV-cache crop/replay and require exact token equality before measuring speed.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Native KV-cache suffix-tree speculative decoding exactness test
- Success threshold: Exact token equality on 100% of benchmark prompts plus at least 1.25x median wall-clock speedup or at least 2x target-forward reduction without increasing peak memory by more than 20%.
- Stop condition: Stop as negative if any exactness mismatch appears after KV-cache replay/cropping is implemented and verified, or if median speedup remains below 1.10x despite at least 0.5 accepted/proposed draft tokens.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-tree-speculative-decoding-vs-exact-no-speculation-on-local-llm-edc3e66591e5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
