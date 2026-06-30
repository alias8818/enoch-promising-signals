# N-gram speculative decoding on CPU without draft model

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-speculative-decoding-on-cpu-without-draft-model-61706656fb62`
Run ID: `n-gram-speculative-decoding-on-cpu-without-draft-model-61706656fb62-20260604T163300823788+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/21130c243385

## What looked useful

Byte/char tokenizations reached about 1.68x to 1.69x median target-invocation upper bound and about 1.44x median speedup under the conservative NumPy proxy. Word tokenization reached only 1.05x median and 1.125x max invocation upper bound, with no rows above 1.0x under 0.1 marginal-cost sensitivity.

## Boundaries and scale limits

No real LLM tokenizer or target model was run. CPU wall-clock speedup was proxied with a toy NumPy decoder-block benchmark at context 4096, d_model 512, d_ff 2048. Corpora were limited to 20000 tokens per tokenization and one prompt/decode size in the main grid.

## Claim scope

Bounded trace simulation on three public text corpora shows exact n-gram prompt lookup without a draft model can reduce target verification iterations for byte/character token streams, but produces only weak gains for simple word-token streams.

## Why it stopped

The evidence is a trace/proxy result, not direct LLM serving evidence. It supports the mechanism for byte/char streams but does not support a broad CPU LLM speedup claim.

## Recommended next action

Stop this run as no-paper useful signal; next bounded action is a direct CPU decoding benchmark with a real small autoregressive model, its tokenizer, prompt-lookup drafting, greedy baseline, and wall-clock tokens/s.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct CPU prompt-lookup decoding benchmark with a real tokenizer and small model
- Success threshold: At least 1.15x median wall-clock tokens/s over greedy baseline on repetitive prompts with identical generated tokens and no regression below 0.98x on low-repetition controls.
- Stop condition: Stop if accepted draft tokens remain below 0.05 per iteration or wall-clock speedup is below 1.05x after a smoke and a medium benchmark.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-speculative-decoding-on-cpu-without-draft-model-61706656fb62`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
