# AnchorState: Agent-Controlled Memory Segmentation via Exact Tokens

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `anchorstate-agent-controlled-memory-segmentation-via-exact-tokens-c35c2638701a`
Run ID: `anchorstate-agent-controlled-memory-segmentation-via-exact-tokens-c35c2638701a-20260520T132708153822+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/b5f6da419786

## What looked useful

Exact special-token anchors were 1 token per boundary versus 8-9 tokens for text delimiters and had 91.25% all-segments exact recovery at 1% boundary-token drop versus 46.75% for natural headers and 53.75% for ASCII anchors. Adversarial in-payload delimiter collisions affected all schemes unless reserved-boundary filtering was applied.

## Boundaries and scale limits

No LLM was prompted, trained, or evaluated. The run used 8 synthetic segments, 2000 deterministic trials, cl100k_base plus locally registered special tokens, and an isolated boundary-token drop simulation. It does not validate real agent memory updates, summarization persistence, tokenizer deployment, or downstream task accuracy.

## Claim scope

Tokenizer/parser proxy evidence: registered exact special-token anchors reduce segment-boundary token overhead and improve synthetic boundary-loss parse recovery compared with natural-language and ASCII text delimiters, provided reserved-boundary filtering is enforced.

## Why it stopped

No-paper useful signal: this was a synthetic tokenizer/parser proxy that supports the mechanism but is not direct publication-grade evidence.

## Recommended next action

Run a bounded model-in-the-loop follow-up where a small local LM must emit, update, and retrieve segmented memory using reserved exact anchors versus natural headers, measuring parse validity and retrieval accuracy over repeated turns.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Model-in-the-loop AnchorState memory persistence test
- Success threshold: Exact-anchor condition improves invalid parse rate by at least 50% relative to natural headers while matching or improving retrieval accuracy and using fewer boundary tokens.
- Stop condition: Stop if exact anchors cannot be reliably emitted by the model/runtime, if parse-validity does not improve by at least 20% in the first bounded run, or if retrieval accuracy drops by more than 5 percentage points versus the best baseline.

## Evidence references

- Artifact root: `<local-path>/projects/anchorstate-agent-controlled-memory-segmentation-via-exact-tokens-c35c2638701a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
