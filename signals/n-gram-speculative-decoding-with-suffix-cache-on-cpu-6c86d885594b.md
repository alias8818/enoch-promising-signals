# N-gram speculative decoding with suffix cache on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-speculative-decoding-with-suffix-cache-on-cpu-6c86d885594b`
Run ID: `n-gram-speculative-decoding-with-suffix-cache-on-cpu-6c86d885594b-20260607T203341308042+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/69fa459122a8

## What looked useful

A bounded suffix cache can reduce target passes substantially on ordered repetitive traces (6.95x synthetic, 2.05x repeated controller prompts, 1.53x small code/docs), while shuffled and unique-token controls collapse to about 1.0x. On 50k Moby-Dick natural prose the trace-level gain is only 1.10x before real verification overhead, so the method is workload-specialized rather than broadly validated.

## Boundaries and scale limits

No real transformer or llama.cpp integration was run; the result measures exact trace acceptance and target-pass reduction, not end-to-end tokens/sec. Natural-language evidence is limited to a 50k-token Moby-Dick slice, and code/docs evidence is only 4.7k local tokens.

## Claim scope

Trace-level CPU evaluation of a bounded online n-gram suffix cache for greedy speculative-decoding accounting on synthetic repetitive text, unique-token controls, repeated controller prompts, small local code/docs text, and 50k Moby-Dick tokens.

## Why it stopped

Trace-level evidence supports a narrow repetition mechanism but does not provide publication-grade or broad end-to-end CPU LLM acceleration evidence.

## Recommended next action

Stop this run as no-paper trace evidence; the next concrete test is direct CPU decoder integration on repetitive code/log/prompt workloads with an exact greedy-output baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end CPU suffix-cache speculative decoding on repetitive code/log prompts
- Success threshold: At least 10% end-to-end tokens/sec improvement on two repetitive real-workload datasets with exact greedy-output preservation and less than 5% slowdown on controls.
- Stop condition: Stop if accepted-token gains fail to overcome verifier/cache overhead or if exact greedy-output preservation breaks.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-speculative-decoding-with-suffix-cache-on-cpu-6c86d885594b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
