# Syllable tokenization for 2x effective long context on CPU

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `syllable-tokenization-for-2x-effective-long-context-on-cpu-9edf0004b11c`
Run ID: `syllable-tokenization-for-2x-effective-long-context-on-cpu-9edf0004b11c-20260528T174450916862+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `38`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/0c44e0cde6a7

## What looked useful

The necessary compression premise for 2x effective context failed: syllable lower-bound tokens were 431,918 versus 416,313 GPT-2 BPE tokens and 377,336 local 50k BPE tokens. The aggregate ratio was 1.0375x GPT-2 BPE, far from the <=0.5x threshold required for 2x context.

## Boundaries and scale limits

No language model was trained; no perplexity or downstream long-context evaluation was run; syllables were estimated rather than implemented as a fully reversible production tokenizer. The test is a favorable lower-bound proxy for sequence length, not full model validation.

## Claim scope

Early CPU-only compression test for English prose: an estimated syllable-token lower bound was compared with GPT-2 BPE and a locally trained 50k byte-level BPE over 1.56M public-domain characters.

## Why it stopped

Proxy/early falsification: even a favorable non-reversible syllable lower bound used slightly more sequence positions than GPT-2 BPE on English prose, so the 2x effective-context premise is not supported.

## Recommended next action

Stop this line as an early proxy falsification unless a new reversible tokenizer specification can first demonstrate <=0.5x modern BPE token count on broad English corpora.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/syllable-tokenization-for-2x-effective-long-context-on-cpu-9edf0004b11c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
